import { createBrowserRouter } from "react-router-dom";
import Dashboard from "pages/Dashboard";
import GenericTestsAll from "pages/GenericTestsAll";

// eslint-disable-next-line import/prefer-default-export
export const router = createBrowserRouter([
    {
        path: "/",
        element: <Dashboard />,
    },
    {
        path: "/login",
        element: <h1>Login</h1>,
    },
    {
        path: "/add-new-deck",
        element: <h1>Add new deck</h1>,
    },
    {
        path: "/library",
        element: <h1>Library</h1>,
    },
    {
        path: "/statistics",
        element: <h1>Statistics</h1>,
    },
    {
        path: "/marketplace",
        element: <h1>Marketplace</h1>,
    },
    {
        path: "/train",
        element: <h1>Train Deck</h1>,
    },
    {
        path: "/tests",
        element: <GenericTestsAll />,
    },
]);
