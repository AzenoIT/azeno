import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AuthConfig, AuthTokenProvider } from "modules/common/AuthToken";
import FakerTest from "./modules/genericTests/FakerTest";

function App() {
    const queryClient = new QueryClient();
    const authConfig: AuthConfig = { tokenEndpoint: "/api/v1/token/" };

    return (
        <QueryClientProvider client={queryClient}>
            <AuthTokenProvider config={authConfig}>
                <FakerTest />
            </AuthTokenProvider>
        </QueryClientProvider>
    );
}

export default App;
