import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AuthTokenProvider, AuthConfig } from "modules/common/AuthToken";
import TestQuery from "modules/common/components/TestQuery/TestQuery";

function App() {
    const queryClient = new QueryClient();
    const authConfig: AuthConfig = { tokenEndpoint: "/api/v1/token/" };

    return (
        <QueryClientProvider client={queryClient}>
            <AuthTokenProvider config={authConfig}>
                <TestQuery />
            </AuthTokenProvider>
        </QueryClientProvider>
    );
}

export default App;
