import { faker } from "@faker-js/faker";
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { AnonymousUserData } from "modules/common/Auth/types";
import useAuth from "modules/common/Auth/useAuth/useAuth";
import { loginAnonymousPlayer, refreshAccessToken, registerAnonymousPlayer } from "modules/common/Auth/useAuth/utils";
import { CreateAuthorizationTokenResponse } from "modules/common/types";
import { beforeEach, describe, Mock, test, vi } from "vitest";

vi.mock("modules/common/Auth/useAuth/utils");

describe("useAuth", () => {
    let username: string;
    let accessToken: string;
    let refreshToken: string;
    let tokenResponse: CreateAuthorizationTokenResponse;
    let anonymousUserData: AnonymousUserData;

    beforeEach(() => {
        username = faker.random.word();
        accessToken = faker.datatype.uuid();
        refreshToken = faker.datatype.uuid();
        tokenResponse = {
            access_token: accessToken,
            refresh_token: refreshToken,
            expires_at: new Date(Date.now() + 60_000).toISOString(),
            refresh_expires_at: new Date(Date.now() + 60 * 60_000).toISOString(),
            token_type: "Bearer",
            scope: [],
            session_state: faker.datatype.uuid(),
        };
        anonymousUserData = {
            id: faker.datatype.uuid(),
            username,
        };

        vi.resetAllMocks();
        localStorage.removeItem("authToken");
        localStorage.removeItem("userData");
        return () => {
            localStorage.removeItem("authToken");
            localStorage.removeItem("userData");
        };
    });

    function UseAuthConsumer() {
        const {
            accessToken: accessToken_,
            refreshToken: refreshToken_,
            refreshAccessToken: refreshAccessToken_,
            isTokenValid,
            isRefreshTokenValid,
            getUserDetail,
            loginAnonymous,
            // setUserDetail,
        } = useAuth();

        return (
            <div>
                <h2 data-testid="accessToken">{accessToken_}</h2>
                <h2 data-testid="refreshToken">{refreshToken_}</h2>
                <h2 data-testid="isTokenValid">{isTokenValid() ? "true" : "false"}</h2>
                <h2 data-testid="isRefreshTokenValid">{isRefreshTokenValid() ? "true" : "false"}</h2>
                <h2 data-testid="getUserDetail">{getUserDetail()?.username || ""}</h2>
                <button type="button" onClick={refreshAccessToken_}>
                    refreshAccessToken
                </button>
                <button type="button" onClick={loginAnonymous}>
                    loginAnonymous
                </button>
                {/* <button */}
                {/*    type="button" */}
                {/*    onClick={() => */}
                {/*        setUserDetail({ */}
                {/*            userType: "anonymous", */}
                {/*            data: { id: "42", username: "Jaro" }, */}
                {/*        }) */}
                {/*    } */}
                {/* > */}
                {/*    setUserDetail */}
                {/* </button> */}
            </div>
        );
    }

    test("without any setup returns default values", () => {
        render(<UseAuthConsumer />);

        expect(screen.getByTestId("accessToken").textContent).toBe("");
        expect(screen.getByTestId("refreshToken").textContent).toBe("");
        expect(screen.getByTestId("isTokenValid").textContent).toBe("false");
        expect(screen.getByTestId("isRefreshTokenValid").textContent).toBe("false");
        expect(screen.getByTestId("getUserDetail").textContent).toBe("");
    });

    test("isRefreshTokenValid returns true if refresh token is valid", () => {
        localStorage.setItem(
            "authToken",
            JSON.stringify({
                refreshExpiresAt: new Date(Date.now() + 60 * 1000),
                refreshToken: "ValidRefresh",
            })
        );
        render(<UseAuthConsumer />);
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
        render(<UseAuthConsumer />);
        expect(screen.getByTestId("isTokenValid").textContent).toBe("true");
    });

    test("refreshAccessToken updates access tokens", async () => {
        (refreshAccessToken as Mock).mockReturnValueOnce(Promise.resolve(tokenResponse));
        render(<UseAuthConsumer />);

        await userEvent.click(screen.getByText("refreshAccessToken"));

        await waitFor(() => expect(screen.getByTestId("accessToken").textContent).toBe(accessToken));
        expect(screen.getByTestId("refreshToken").textContent).toBe(refreshToken);
    });

    test("getUserData returns non value from localStorage if present", () => {
        localStorage.setItem("userData", JSON.stringify({ userType: "anonymous", data: anonymousUserData }));
        render(<UseAuthConsumer />);
        expect(screen.getByTestId("getUserDetail").textContent).toBe(username);
    });

    test("loginAnonymous updates access tokens", async () => {
        (loginAnonymousPlayer as Mock).mockReturnValueOnce(Promise.resolve(tokenResponse));
        localStorage.setItem("userData", JSON.stringify({ userType: "anonymous", data: anonymousUserData }));
        render(<UseAuthConsumer />);

        await userEvent.click(screen.getByText("loginAnonymous"));

        await waitFor(() => expect(screen.getByTestId("accessToken").textContent).toBe(accessToken));
        expect(screen.getByTestId("refreshToken").textContent).toBe(refreshToken);
    });

    test("register updates authData and access tokens", async () => {
        (registerAnonymousPlayer as Mock).mockReturnValueOnce(Promise.resolve(anonymousUserData));

        render(<UseAuthConsumer />);
    });

    // test("login sends request to login endpoint", async () => {
    //     server.use(
    //         rest.post("http://localhost/api/v1/token/", async (req, res, ctx) => {
    //             const data = await req.json();
    //             if (data.username !== username || data.password !== password) return res(ctx.status(401));
    //             return res(
    //                 ctx.status(200),
    //                 ctx.json({
    //                     access_token: "NewAccessToken",
    //                     refresh_token: "NewRefreshToken",
    //                     expires_at: new Date(Date.now() + 60_000),
    //                     refresh_expires_at: new Date(Date.now() + 60 * 60_000),
    //                 })
    //             );
    //         })
    //     );
    //     render(<UseAuthConsumer/>);
    //
    //     expect(screen.getByTestId("accessToken").textContent).toBe("");
    //     expect(screen.getByTestId("refreshToken").textContent).toBe("");
    //     expect(screen.getByTestId("isTokenValid").textContent).toBe("false");
    //     expect(screen.getByTestId("isRefreshTokenValid").textContent).toBe("false");
    //
    //     await userEvent.click(screen.getByText("login"));
    //     await waitFor(() => expect(screen.getByTestId("accessToken").textContent).toBe("NewAccessToken"));
    //     expect(screen.getByTestId("refreshToken").textContent).toBe("NewRefreshToken");
    //     expect(screen.getByTestId("isTokenValid").textContent).toBe("true");
    //     expect(screen.getByTestId("isRefreshTokenValid").textContent).toBe("true");
    // });
    //
    // test("getUserData returns non value from localStorage if present", () => {
    //     localStorage.setItem(
    //         "userData",
    //         JSON.stringify({
    //             userType: "anonymous",
    //             data: {
    //                 id: "11",
    //                 username: "Rex",
    //             },
    //         })
    //     );
    //     render(<UseAuthConsumer/>);
    //     expect(screen.getByTestId("getUserDetail").textContent).toBe("Rex");
    // });
    //
    // test("getUserData updates value in localStorage", async () => {
    //     render(<UseAuthConsumer/>);
    //
    //     expect(screen.getByTestId("getUserDetail").textContent).toBe("");
    //     await userEvent.click(screen.getByText("setUserDetail"));
    //     await waitFor(() => expect(screen.getByTestId("getUserDetail").textContent).toBe("Jaro"));
    // });
});
