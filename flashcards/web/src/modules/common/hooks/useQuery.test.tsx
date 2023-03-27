import { QueryClient, QueryClientProvider, useQuery } from "@tanstack/react-query";
import { render, screen, waitFor } from "@testing-library/react";
import axios from "axios";
import { server } from "mocks/server";
import { rest } from "msw";
import { describe, expect } from "vitest";

describe("useQuery", () => {
    function UseQueryClient() {
        const { data = "", isLoading } = useQuery<string>({
            queryKey: ["test"],
            queryFn: async () => {
                const response = await axios.get("/api/v1/test/");
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
                <UseQueryClient />
            </QueryClientProvider>
        );
    }

    test("properly fetches data", async () => {
        server.use(
            rest.get("http://localhost/api/v1/test/", (_, res, ctx) => {
                return res(ctx.status(200), ctx.json("42"));
            })
        );

        renderHook();

        expect(screen.getByTestId("ResponseData").textContent).toBe("");
        await waitFor(() => expect(screen.getByTestId("LoadingStatus").textContent).toBe("true"));
        await waitFor(() => expect(screen.getByTestId("LoadingStatus").textContent).toBe("false"));
        await waitFor(() => expect(screen.getByTestId("ResponseData").textContent).toBe("42"));
    });
});
