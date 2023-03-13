import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AuthConfig, AuthTokenProvider } from "modules/common/AuthToken";
import FakerTest from "./components/FakerTest/FakerTest";
import TailwindTest from "./components/TailwindTest/TailwindTest";

function App() {
    const queryClient = new QueryClient();
    const authConfig: AuthConfig = { tokenEndpoint: "/api/v1/token/" };

    return (
        <QueryClientProvider client={queryClient}>
            <AuthTokenProvider config={authConfig}>
                <>
                    <TailwindTest />
                    <FakerTest />
                </>
            </AuthTokenProvider>
        </QueryClientProvider>
    );
}

export default App;
