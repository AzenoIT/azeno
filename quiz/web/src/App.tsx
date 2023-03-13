import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AuthConfig, AuthTokenProvider } from "modules/common/AuthToken";
import TailwindTest from "modules/genericTests/TailwindTest/TailwindTest";
import FormikTest from "modules/genericTests/FormikTest/FormikTest";

function App() {
    const queryClient = new QueryClient();
    const authConfig: AuthConfig = { tokenEndpoint: "/api/v1/token/" };

    return (
        <QueryClientProvider client={queryClient}>
            <AuthTokenProvider config={authConfig}>
                <>
                    <h1>Hello World</h1>
                    <TailwindTest />
                    <FormikTest />
                </>
            </AuthTokenProvider>
        </QueryClientProvider>
    );
}

export default App;
