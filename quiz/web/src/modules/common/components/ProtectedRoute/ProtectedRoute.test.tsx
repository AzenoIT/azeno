import { render, screen, waitFor } from "@testing-library/react";
import { AuthTokenProvider } from "modules/common/AuthToken";
import ProtectedRoute from "modules/common/components/ProtectedRoute/ProtectedRoute";
import { MemoryRouter, Route, Routes } from "react-router-dom";
import { beforeEach, describe, test } from "vitest";

describe("ProtectedRoute", () => {
    function RenderProtectedRoute() {
        render(
            <AuthTokenProvider config={{ loginEndpoint: "/", refreshEndpoint: "/refresh/" }}>
                <MemoryRouter>
                    <Routes>
                        <Route
                            path="/"
                            element={
                                <ProtectedRoute>
                                    <h1>Protected Route</h1>
                                </ProtectedRoute>
                            }
                        />
                        <Route path="/login" element={<h1>Login</h1>} />
                    </Routes>
                </MemoryRouter>
            </AuthTokenProvider>
        );
    }

    beforeEach(() => {
        localStorage.removeItem("authToken");
        return () => localStorage.removeItem("authToken");
    });

    test("redirects to login if token is expired or not present", async () => {
        RenderProtectedRoute();

        await waitFor(() => expect(screen.getByText("Login")));
    });

    test("does nothing if token is present", async () => {
        localStorage.setItem(
            "authToken",
            JSON.stringify({
                expiresAt: new Date(Date.now() + 60 * 1000),
                accessToken: "ValidToken",
                refreshExpiresAt: new Date(Date.now() + 60 * 60 * 1000),
                refreshToken: "ValidRefresh",
            })
        );
        RenderProtectedRoute();

        await waitFor(() => expect(screen.getByText("Protected Route")));
    });
});
