import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import ErrorBoundary from "modules/common/components/ErrorBoundary";
import { RouterProvider } from "react-router-dom";
import { router } from "router";
import TestBank from "./modules/genericTests/TestBank";

function App() {
    const queryClient = new QueryClient();

    return (
        <QueryClientProvider client={queryClient}>
            <ErrorBoundary>
                <TestBank />
                <RouterProvider router={router} />
            </ErrorBoundary>
        </QueryClientProvider>
    );
}

export default App;
