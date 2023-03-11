import { describe, test } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import useAuthToken from "modules/common/AuthToken/useAuthToken/useAuthToken";
import { AuthTokenProvider } from "modules/common/AuthToken/AuthTokenProvider";
import { server } from "mocks/server";
import { rest } from "msw";

describe("useAuthToken", () => {
    function UseAuthTokenRendered() {
        const { accessToken, refreshToken, refreshAccessToken, setAccessToken, setRefreshToken, setTokens } =
            useAuthToken();

        return (
            <div>
                <h2 data-testid="accessToken">{accessToken}</h2>
                <h2 data-testid="refreshToken">{refreshToken}</h2>
                <button type="button" onClick={refreshAccessToken}>
                    refreshAccessToken
                </button>
                <button type="button" onClick={() => setAccessToken("21")}>
                    setAccessToken
                </button>
                <button type="button" onClick={() => setRefreshToken("42")}>
                    setRefreshToken
                </button>
                <button
                    type="button"
                    onClick={() => setTokens({ accessToken: "accessToken", refreshToken: "refreshToken" })}
                >
                    setTokens
                </button>
            </div>
        );
    }

    function renderUseAuthToken() {
        render(
            <AuthTokenProvider config={{ tokenEndpoint: "/api/v1/token/" }}>
                <UseAuthTokenRendered />
            </AuthTokenProvider>
        );
    }

    test("without any setup returns both tokens as empty strings", () => {
        renderUseAuthToken();

        expect(screen.getByTestId("accessToken").textContent).toBe("");
        expect(screen.getByTestId("refreshToken").textContent).toBe("");
    });

    test("setAccessToken updates token", async () => {
        renderUseAuthToken();

        await userEvent.click(screen.getByText("setAccessToken"));

        await waitFor(() => expect(screen.getByTestId("accessToken").textContent).toBe("21"));
    });

    test("setRefreshToken updates token", async () => {
        renderUseAuthToken();
        await userEvent.click(screen.getByText("setRefreshToken"));

        await waitFor(() => expect(screen.getByTestId("refreshToken").textContent).toBe("42"));
    });

    test("setTokens updates both tokens", async () => {
        renderUseAuthToken();

        await userEvent.click(screen.getByText("setTokens"));

        await waitFor(() => expect(screen.getByTestId("accessToken").textContent).toBe("accessToken"));
        expect(screen.getByTestId("refreshToken").textContent).toBe("refreshToken");
    });

    test("refreshToken sends request to reload token", async () => {
        server.use(
            rest.post("http://localhost/api/v1/token/", (_, res, ctx) => {
                return res(ctx.status(200), ctx.json({ access_token: "NewAccessToken" }));
            })
        );
        renderUseAuthToken();

        await userEvent.click(screen.getByText("refreshAccessToken"));

        await waitFor(() => expect(screen.getByTestId("accessToken").textContent).toBe("NewAccessToken"));
    });
});
