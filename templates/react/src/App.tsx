import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import ErrorBoundary from "modules/common/components/ErrorBoundary";
import { RouterProvider } from "react-router-dom";
import { router } from "router";

function App() {
    const queryClient = new QueryClient();

    return (
        <QueryClientProvider client={queryClient}>
            <ErrorBoundary>
                <RouterProvider router={router} />
            </ErrorBoundary>
        </QueryClientProvider>
    );
}

export default App;
