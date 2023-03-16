import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { server } from "mocks/server";
import { AuthTokenProvider } from "modules/common/AuthToken/AuthTokenProvider";
import useAuthToken from "modules/common/AuthToken/useAuthToken/useAuthToken";
import { rest } from "msw";
import { beforeEach, describe, test } from "vitest";

describe("useAuthToken", () => {
    const username = "testUser";
    const password = "testPass";

    function UseAuthTokenRendered() {
        const { accessToken, refreshToken, refreshAccessToken, isTokenValid, isRefreshTokenValid, login } =
            useAuthToken();

        return (
            <div>
                <h2 data-testid="accessToken">{accessToken}</h2>
                <h2 data-testid="refreshToken">{refreshToken}</h2>
                <h2 data-testid="isTokenValid">{isTokenValid() ? "true" : "false"}</h2>
                <h2 data-testid="isRefreshTokenValid">{isRefreshTokenValid() ? "true" : "false"}</h2>
                <button type="button" onClick={refreshAccessToken}>
                    refreshAccessToken
                </button>
                <button type="button" onClick={() => login(username, password)}>
                    login
                </button>
            </div>
        );
    }

    function renderUseAuthToken() {
        render(
            <AuthTokenProvider config={{ loginEndpoint: "/api/v1/token/", refreshEndpoint: "/api/v1/token/refresh/" }}>
                <UseAuthTokenRendered />
            </AuthTokenProvider>
        );
    }

    beforeEach(() => {
        localStorage.removeItem("authToken");
        return () => localStorage.removeItem("authToken");
    });

    test("without any setup returns default values", () => {
        renderUseAuthToken();

        expect(screen.getByTestId("accessToken").textContent).toBe("");
        expect(screen.getByTestId("refreshToken").textContent).toBe("");
        expect(screen.getByTestId("isTokenValid").textContent).toBe("false");
        expect(screen.getByTestId("isRefreshTokenValid").textContent).toBe("false");
    });

    test("refreshToken sends request to reload token", async () => {
        server.use(
            rest.post("http://localhost/api/v1/token/refresh/", (_, res, ctx) => {
                return res(ctx.status(200), ctx.json({ access_token: "NewAccessToken" }));
            })
        );
        renderUseAuthToken();

        await userEvent.click(screen.getByText("refreshAccessToken"));

        await waitFor(() => expect(screen.getByTestId("accessToken").textContent).toBe("NewAccessToken"));
    });

    test("isRefreshTokenValid returns true if refresh token is valid", () => {
        localStorage.setItem(
            "authToken",
            JSON.stringify({
                refreshExpiresAt: new Date(Date.now() + 60 * 1000),
                refreshToken: "ValidRefresh",
            })
        );
        renderUseAuthToken();
        expect(screen.getByTestId("isRefreshTokenValid").textContent).toBe("true");
    });

    test("isTokenValid returns true if access token is valid", () => {
        localStorage.setItem(
            "authToken",
            JSON.stringify({
                expiresAt: new Date(Date.now() + 60 * 1000),
                accessToken: "ValidToken",
                refreshExpiresAt: new Date(Date.now() + 60 * 60 * 1000),
                refreshToken: "ValidRefresh",
            })
        );
        renderUseAuthToken();
        expect(screen.getByTestId("isTokenValid").textContent).toBe("true");
    });

    test("login sends request to login endpoint", async () => {
        server.use(
            rest.post("http://localhost/api/v1/token/", async (req, res, ctx) => {
                const data = await req.json();
                if (data.username !== username || data.password !== password) return res(ctx.status(401));
                return res(
                    ctx.status(200),
                    ctx.json({
                        access_token: "NewAccessToken",
                        refresh_token: "NewRefreshToken",
                        expires_at: new Date(Date.now() + 60_000),
                        refresh_expires_at: new Date(Date.now() + 60 * 60_000),
                    })
                );
            })
        );
        renderUseAuthToken();

        expect(screen.getByTestId("accessToken").textContent).toBe("");
        expect(screen.getByTestId("refreshToken").textContent).toBe("");
        expect(screen.getByTestId("isTokenValid").textContent).toBe("false");
        expect(screen.getByTestId("isRefreshTokenValid").textContent).toBe("false");

        await userEvent.click(screen.getByText("login"));
        await waitFor(() => expect(screen.getByTestId("accessToken").textContent).toBe("NewAccessToken"));
        expect(screen.getByTestId("refreshToken").textContent).toBe("NewRefreshToken");
        expect(screen.getByTestId("isTokenValid").textContent).toBe("true");
        expect(screen.getByTestId("isRefreshTokenValid").textContent).toBe("true");
    });
});
