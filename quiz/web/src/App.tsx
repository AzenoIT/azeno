import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AuthConfig, AuthTokenProvider } from "modules/common/AuthToken";
import ErrorBoundary from "modules/common/components/ErrorBoundary";
import { BrowserRouter, createBrowserRouter, RouterProvider } from "react-router-dom";

const router = createBrowserRouter([
    {
        path: "/",
        element: <h1>Home</h1>,
    },
    {
        path: "/login",
        element: <h1>Login</h1>,
    },
]);

function App() {
    const queryClient = new QueryClient();
    const authConfig: AuthConfig = { loginEndpoint: "/api/v1/token/", refreshEndpoint: "/api/v1/token/refresh/" };

    return (
        <QueryClientProvider client={queryClient}>
            <AuthTokenProvider config={authConfig}>
                <BrowserRouter>
                    <ErrorBoundary>
                        <RouterProvider router={router} />
                    </ErrorBoundary>
                </BrowserRouter>
            </AuthTokenProvider>
        </QueryClientProvider>
    );
}

export default App;
