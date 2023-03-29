import { render, screen, waitFor } from "@testing-library/react";
import { AuthProvider } from "modules/common/Auth";
import PlayerRequired from "modules/common/components/PlayerRequired/PlayerRequired";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { beforeEach, describe, test } from "vitest";

describe("PlayerRequired", () => {
    function RenderUserRequired() {
        render(
            <AuthProvider config={{ loginEndpoint: "/", refreshEndpoint: "/refresh/" }}>
                <MemoryRouter>
                    <Routes>
                        <Route
                            path="/"
                            element={
                                <PlayerRequired>
                                    <h1>Protected Route</h1>
                                </PlayerRequired>
                            }
                        />
                        <Route path="/start" element={<h1>Login</h1>} />
                    </Routes>
                </MemoryRouter>
            </AuthProvider>
        );
    }

    beforeEach(() => {
        localStorage.removeItem("userData");
        return () => localStorage.removeItem("userData");
    });

    test("redirects to login if token is expired or not present", async () => {
        RenderUserRequired();

        await waitFor(() => expect(screen.getByText("Login")));
    });

    test("does nothing if token is present", async () => {
        localStorage.setItem(
            "userData",
            JSON.stringify({
                userType: "anonymous",
                data: {
                    id: "21",
                    username: "Chad",
                },
            })
        );
        RenderUserRequired();

        await waitFor(() => expect(screen.getByText("Protected Route")));
    });
});
