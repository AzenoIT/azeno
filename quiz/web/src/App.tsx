import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AuthConfig, AuthProvider } from "modules/common/Auth";
import ErrorBoundary from "modules/common/components/ErrorBoundary";
import { RouterProvider } from "react-router-dom";
import { router } from "router";

function App() {
    const queryClient = new QueryClient();
    const authConfig: AuthConfig = { loginEndpoint: "/api/v1/token/", refreshEndpoint: "/api/v1/token/refresh/" };

    return (
        <QueryClientProvider client={queryClient}>
            <AuthProvider config={authConfig}>
                <ErrorBoundary>
                    <RouterProvider router={router} />
                </ErrorBoundary>
            </AuthProvider>
        </QueryClientProvider>
    );
}

export default App;
