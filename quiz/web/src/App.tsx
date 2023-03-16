import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AuthConfig, AuthTokenProvider } from "modules/common/AuthToken";
import ErrorBoundary from "modules/common/components/ErrorBoundary";
import { RouterProvider } from "react-router-dom";
import { router } from "router";
import TailwindTest from "modules/genericTests/TailwindTest/TailwindTest";
import FormikTest from "modules/genericTests/FormikTest/FormikTest";

function App() {
    const queryClient = new QueryClient();
    const authConfig: AuthConfig = { loginEndpoint: "/api/v1/token/", refreshEndpoint: "/api/v1/token/refresh/" };

    return (
        <QueryClientProvider client={queryClient}>
            <AuthTokenProvider config={authConfig}>
                <ErrorBoundary>
                    <RouterProvider router={router} />
                    <TailwindTest />
                    <FormikTest />
                </ErrorBoundary>
            </AuthTokenProvider>
        </QueryClientProvider>
    );
}

export default App;
