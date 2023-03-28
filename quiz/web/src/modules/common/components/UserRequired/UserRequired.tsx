import { useAuth } from "modules/common/Auth";
import { Navigate } from "react-router-dom";

export default function UserRequired({ children }: { children: JSX.Element }) {
    const auth = useAuth();

    if (auth.getUserDetail() === null) {
        return <Navigate to="/start" />;
    }
    return children;
}
