import { UserRequired } from "modules/common/components";
import { createBrowserRouter } from "react-router-dom";

// eslint-disable-next-line import/prefer-default-export
export const router = createBrowserRouter([
    {
        path: "/",
        element: (
            <UserRequired>
                <h1>HOME</h1>
            </UserRequired>
        ),
    },
    {
        path: "/start/",
        element: <h1>Start</h1>,
    },
    {
        path: "/login/",
        element: <h1>Login</h1>,
    },
    {
        path: "/register/",
        element: <h1>Register</h1>,
    },
]);
