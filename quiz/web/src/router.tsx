import { createBrowserRouter } from "react-router-dom";

// eslint-disable-next-line import/prefer-default-export
export const router = createBrowserRouter([
    {
        path: "/",
        element: <h1>Home</h1>,
    },
    {
        path: "/login",
        element: <h1>Login</h1>,
    },
]);
