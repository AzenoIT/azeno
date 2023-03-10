import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import TestQuery from "modules/common/components/TestQuery/TestQuery";

function App() {
    const queryClient = new QueryClient();

    return (
        <QueryClientProvider client={queryClient}>
            <TestQuery />
        </QueryClientProvider>
    );
}

export default App;
