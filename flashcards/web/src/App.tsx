import { router } from "router";
import { RouterProvider } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AuthConfig, AuthTokenProvider } from "modules/common/AuthToken";
import ErrorBoundary from "modules/common/components/ErrorBoundary";
import FormikTest from "modules/genericTests/FormikTest/FormikTest";
import TailwindTest from "modules/genericTests/TailwindTest/TailwindTest";
import FakerTest from "modules/genericTests/FakerTest/FakerTest";
import MaterialUITest from "modules/genericTests/MaterialUITest/MaterialUITest";
import AddDecksForm from "components/AddDecksForm";

function App() {
    const queryClient = new QueryClient();
    const authConfig: AuthConfig = { loginEndpoint: "/api/v1/token/", refreshEndpoint: "/api/v1/token/refresh/" };

    return (
        <QueryClientProvider client={queryClient}>
            <AuthTokenProvider config={authConfig}>
                <ErrorBoundary>
                    <RouterProvider router={router} />
                    <FakerTest />
                    <TailwindTest />
                    <FormikTest />
                    <MaterialUITest />
                    <AddDecksForm />
                </ErrorBoundary>
            </AuthTokenProvider>
        </QueryClientProvider>
    );
}

export default App;
