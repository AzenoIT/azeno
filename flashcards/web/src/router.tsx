import { createBrowserRouter } from "react-router-dom";
import Flashcard from "./modules/common/components/Flashcards/Flashcard";

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
    {
        path: "/decks/:id/flashcards",
        element: <Flashcard />,
    },
]);
