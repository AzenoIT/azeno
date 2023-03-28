import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { server } from "mocks/server";
import { AuthProvider } from "modules/common/Auth/AuthProvider";
import useAuth from "modules/common/Auth/useAuth/useAuth";
import { rest } from "msw";
import { beforeEach, describe, test } from "vitest";

describe("useAuth", () => {
    const username = "testUser";
    const password = "testPass";

    function UseAuthRendered() {
        const {
            accessToken,
            refreshToken,
            refreshAccessToken,
            isTokenValid,
            isRefreshTokenValid,
            login,
            getUserDetail,
            setUserDetail,
        } = useAuth();

        return (
            <div>
                <h2 data-testid="accessToken">{accessToken}</h2>
                <h2 data-testid="refreshToken">{refreshToken}</h2>
                <h2 data-testid="isTokenValid">{isTokenValid() ? "true" : "false"}</h2>
                <h2 data-testid="isRefreshTokenValid">{isRefreshTokenValid() ? "true" : "false"}</h2>
                <h2 data-testid="getUserDetail">{getUserDetail()?.username || ""}</h2>
                <button type="button" onClick={refreshAccessToken}>
                    refreshAccessToken
                </button>
                <button type="button" onClick={() => login(username, password)}>
                    login
                </button>
                <button
                    type="button"
                    onClick={() =>
                        setUserDetail({
                            userType: "anonymous",
                            data: { id: "42", username: "Jaro" },
                        })
                    }
                >
                    setUserDetail
                </button>
            </div>
        );
    }

    function RenderUseAuth() {
        render(
            <AuthProvider config={{ loginEndpoint: "/api/v1/token/", refreshEndpoint: "/api/v1/token/refresh/" }}>
                <UseAuthRendered />
            </AuthProvider>
        );
    }

    beforeEach(() => {
        localStorage.removeItem("authToken");
        localStorage.removeItem("userData");
        return () => {
            localStorage.removeItem("authToken");
            localStorage.removeItem("userData");
        };
    });

    test("without any setup returns default values", () => {
        RenderUseAuth();

        expect(screen.getByTestId("accessToken").textContent).toBe("");
        expect(screen.getByTestId("refreshToken").textContent).toBe("");
        expect(screen.getByTestId("isTokenValid").textContent).toBe("false");
        expect(screen.getByTestId("isRefreshTokenValid").textContent).toBe("false");
        expect(screen.getByTestId("getUserDetail").textContent).toBe("");
    });

    test("refreshToken sends request to reload token", async () => {
        server.use(
            rest.post("http://localhost/api/v1/token/refresh/", (_, res, ctx) => {
                return res(ctx.status(200), ctx.json({ access_token: "NewAccessToken" }));
            })
        );
        RenderUseAuth();

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
        RenderUseAuth();
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
        RenderUseAuth();
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
        RenderUseAuth();

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

    test("getUserData returns non value from localStorage if present", () => {
        localStorage.setItem(
            "userData",
            JSON.stringify({
                userType: "anonymous",
                data: {
                    id: "11",
                    username: "Rex",
                },
            })
        );
        RenderUseAuth();
        expect(screen.getByTestId("getUserDetail").textContent).toBe("Rex");
    });

    test("getUserData updates value in localStorage", async () => {
        RenderUseAuth();

        expect(screen.getByTestId("getUserDetail").textContent).toBe("");
        await userEvent.click(screen.getByText("setUserDetail"));
        await waitFor(() => expect(screen.getByTestId("getUserDetail").textContent).toBe("Jaro"));
    });
});
