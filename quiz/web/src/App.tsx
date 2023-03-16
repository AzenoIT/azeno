import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AuthConfig, AuthTokenProvider } from "modules/common/AuthToken";
import MaterialUiTest from "./components/MaterialUiTest/MaterialUiTest";

function App() {
    const queryClient = new QueryClient();
    const authConfig: AuthConfig = { tokenEndpoint: "/api/v1/token/" };

    return (
        <QueryClientProvider client={queryClient}>
            <AuthTokenProvider config={authConfig}>
                <MaterialUiTest />
            </AuthTokenProvider>
        </QueryClientProvider>
    );
}

export default App;
