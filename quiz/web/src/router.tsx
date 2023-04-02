import { PlayerRequired } from "modules/common/components";
import Start from "modules/Start/Start";
import { createBrowserRouter } from "react-router-dom";

// eslint-disable-next-line import/prefer-default-export
export const router = createBrowserRouter([
    {
        path: "/",
        element: (
            <PlayerRequired>
                <h1>HOME</h1>
            </PlayerRequired>
        ),
    },
    {
        path: "/start/",
        element: <Start />,
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
