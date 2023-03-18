import { router } from "router";
import { RouterProvider } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AuthConfig, AuthTokenProvider } from "modules/common/AuthToken";
import ErrorBoundary from "modules/common/components/ErrorBoundary";

import FakerTest from "modules/genericTests/FakerTest/FakerTest";
import FormikTest from "modules/genericTests/FormikTest/FormikTest";
import TailwindTest from "modules/genericTests/TailwindTest/TailwindTest";
import TranslationTest from "modules/genericTests/TranslationTest/TranslationTest";
import LanguageSwitcher from "modules/genericTests/LanguageSwitcher/LanguageSwitcher";

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
                    <TranslationTest />
                    <LanguageSwitcher />
                </ErrorBoundary>
            </AuthTokenProvider>
        </QueryClientProvider>
    );
}

export default App;
