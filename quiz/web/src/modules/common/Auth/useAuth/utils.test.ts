import { faker } from "@faker-js/faker";

import { server } from "mocks/server";
import { player } from "modules/common/api_urls";
import { AnonymousUserData } from "modules/common/Auth/types";
import { registerAnonymousUser } from "modules/common/Auth/useAuth/utils";
import { rest } from "msw";
import { describe, test } from "vitest";

describe("registerAnonymousUser", () => {
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
            rest.post(player.register, (_, res, ctx) => {
                return res(ctx.status(201), ctx.json(userData));
            })
        );

        const response = await registerAnonymousUser(username);

        expect(response).toMatchObject(userData);
    });
});
