import { faker } from "@faker-js/faker";
import { server } from "mocks/server";
import { player, token } from "modules/common/apiUrls";
import { AnonymousUserData } from "modules/common/Auth/types";
import { loginAnonymousPlayer, refreshAccessToken, registerAnonymousPlayer } from "modules/common/Auth/useAuth/utils";
import { CreateAuthorizationTokenResponse } from "modules/common/types";
import { rest } from "msw";
import { describe, test } from "vitest";

describe("registerPlayer", () => {
    let userData: AnonymousUserData;
    let username: string;

    beforeEach(() => {
        username = faker.internet.userName();
        userData = {
            id: faker.datatype.uuid(),
            username,
        };
    });

    test("sends request to correct endpoint", async () => {
        server.use(
            rest.post(player.register(), (_, res, ctx) => {
                return res(ctx.status(201), ctx.json(userData));
            })
        );

        const response = await registerAnonymousPlayer(username);

        expect(response).toMatchObject(userData);
    });

    test("handling error caused by invalid username", async () => {
        server.use(
            rest.post(player.register(), (_, res, ctx) => {
                return res(ctx.status(406), ctx.json({ message: "Invalid username." }));
            })
        );

        await expect(registerAnonymousPlayer(username)).rejects.toThrowError("Invalid username");
    });

    test("handling generic errors", async () => {
        server.use(
            rest.post(player.register(), (_, res, ctx) => {
                return res(ctx.status(400), ctx.json({ message: faker.random.word() }));
            })
        );

        await expect(registerAnonymousPlayer(username)).rejects.toThrowError("Unexpected error has occurred.");
    });
});

describe("loginPlayer", () => {
    let accessToken: string;
    let refreshToken: string;
    let expiresAt: string;
    let refreshExpiresAt: string;
    let tokenResponse: CreateAuthorizationTokenResponse;
    let playerId: string;

    beforeEach(() => {
        accessToken = faker.datatype.uuid();
        refreshToken = faker.datatype.uuid();
        expiresAt = new Date(Date.now() + 60_000).toISOString();
        refreshExpiresAt = new Date(Date.now() + 60 * 60_000).toISOString();
        tokenResponse = {
            access_token: accessToken,
            refresh_token: refreshToken,
            expires_at: expiresAt,
            refresh_expires_at: refreshExpiresAt,
            token_type: "Bearer",
            scope: [],
            session_state: faker.datatype.uuid(),
        };
        playerId = faker.datatype.uuid();
    });

    test("can login anonymous player using uuid", async () => {
        server.use(
            rest.post(token.create(), async (_, res, ctx) => {
                return res(ctx.status(200), ctx.json(tokenResponse));
            })
        );

        const tokens = await loginAnonymousPlayer(playerId);

        expect(tokens.access_token).toBe(accessToken);
        expect(tokens.refresh_token).toBe(refreshToken);
        expect(tokens.expires_at).toBe(expiresAt);
        expect(tokens.refresh_expires_at).toBe(refreshExpiresAt);
    });

    test("error handling for invalid id", async () => {
        server.use(
            rest.post(token.create(), async (_, res, ctx) => {
                return res(ctx.status(401), ctx.json({ message: "Invalid credentials." }));
            })
        );

        await expect(loginAnonymousPlayer(playerId)).rejects.toThrowError("Invalid credentials.");
    });

    test("handling generic errors", async () => {
        server.use(
            rest.post(token.create(), async (_, res, ctx) => {
                return res(ctx.status(407), ctx.json("123"));
            })
        );

        await expect(loginAnonymousPlayer(playerId)).rejects.toThrowError("Unexpected error has occurred.");
    });
});

describe("refreshAccessToken", () => {
    let refreshToken: string;
    let tokenResponse: CreateAuthorizationTokenResponse;

    beforeEach(() => {
        server.restoreHandlers();
        refreshToken = faker.datatype.uuid();
        tokenResponse = {
            access_token: faker.datatype.uuid(),
            refresh_token: faker.datatype.uuid(),
            expires_at: new Date(Date.now() + 60_000).toISOString(),
            refresh_expires_at: new Date(Date.now() + 60 * 60_000).toISOString(),
            token_type: "Bearer",
            scope: [],
            session_state: faker.datatype.uuid(),
        };
    });

    test("can refresh token using refresh_token", async () => {
        server.use(
            rest.post(token.refresh(), (_, res, ctx) => {
                return res(ctx.status(200), ctx.json(tokenResponse));
            })
        );

        const tokens = await refreshAccessToken(refreshToken);

        expect(tokens).toMatchObject(tokenResponse);
    });

    test("error handling for expired refresh token", async () => {
        server.use(
            rest.post(token.refresh(), (_, res, ctx) => {
                return res(ctx.status(401), ctx.json({ message: "Invalid credentials." }));
            })
        );

        await expect(refreshAccessToken(refreshToken)).rejects.toThrowError("Invalid credentials.");
    });

    test("generic error handling", async () => {
        server.use(
            rest.post(token.refresh(), (_, res, ctx) => {
                return res(ctx.status(422));
            })
        );

        await expect(refreshAccessToken(refreshToken)).rejects.toThrowError("Unexpected error has occurred.");
    });
});
