import { faker } from "@faker-js/faker";
import { QueryClient, QueryClientProvider, useQuery } from "@tanstack/react-query";
import { render, screen, waitFor } from "@testing-library/react";
import { server } from "mocks/server";
import { refreshAccessToken } from "modules/common/Auth/useAuth/utils";
import useApiClient from "modules/common/hooks/useApiClient/useApiClient";
import { rest } from "msw";
import { beforeEach, describe, Mock, vi } from "vitest";

vi.mock("modules/common/Auth/useAuth/utils");

describe("useApiClient", () => {
    function UseApiClientClient() {
        const axios = useApiClient();

        const { data = "", isLoading } = useQuery<string>({
            queryKey: ["test"],
            queryFn: async () => {
                const response = await axios.get("/api/v1/protected/");
                return response.data;
            },
        });

        return (
            <div>
                <h2 data-testid="ResponseData">{data}</h2>
                <h2 data-testid="LoadingStatus">{isLoading ? "true" : "false"}</h2>
            </div>
        );
    }

    function renderHook() {
        const client = new QueryClient();
        render(
            <QueryClientProvider client={client}>
                <UseApiClientClient />
            </QueryClientProvider>
        );
    }

    const validAccessToken = "whatIsTheMeaningOfLifeTheUniverseAndEverything";

    beforeEach(() => {
        localStorage.removeItem("authToken");
        server.restoreHandlers();
        server.use(
            rest.get("http://localhost/api/v1/protected/", (req, res, ctx) => {
                if (req.headers.get("Authorization") !== `Bearer ${validAccessToken}`) {
                    return res(ctx.status(403));
                }
                return res(ctx.status(200), ctx.json("42"));
            })
        );
        return () => localStorage.removeItem("authToken");
    });

    test("during request attaches Authorization header", async () => {
        localStorage.setItem("authToken", JSON.stringify({ accessToken: validAccessToken, refreshToken: "12" }));

        renderHook();

        await waitFor(() => expect(screen.getByTestId("ResponseData").textContent).toBe(""));
        await waitFor(() => expect(screen.getByTestId("LoadingStatus").textContent).toBe("false"));
        await waitFor(() => expect(screen.getByTestId("ResponseData").textContent).toBe("42"));
    });

    test("requests new token when 403 is returned", async () => {
        localStorage.setItem("authToken", JSON.stringify({ accessToken: "invalidToken", refreshToken: "12" }));
        (refreshAccessToken as Mock).mockReturnValueOnce({
            access_token: validAccessToken,
            refresh_token: faker.datatype.uuid(),
            expires_at: faker.date.future(),
            refresh_expires_at: faker.date.future(),
        });

        renderHook();

        await waitFor(() => expect(screen.getByTestId("ResponseData").textContent).toBe(""));
        await waitFor(() => expect(screen.getByTestId("LoadingStatus").textContent).toBe("true"));
        await waitFor(() => expect(screen.getByTestId("LoadingStatus").textContent).toBe("false"));
        await waitFor(() => expect(screen.getByTestId("ResponseData").textContent).toBe("42"));
        expect(JSON.parse(localStorage.getItem("authToken") || "").accessToken).toBe(validAccessToken);
    });
});
