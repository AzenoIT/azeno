import { useAuthToken } from "modules/common/AuthToken";
import { Navigate } from "react-router-dom";

export default function ProtectedRoute({ children }: { children: JSX.Element }) {
    const authToken = useAuthToken();

    if (!authToken.isTokenValid()) {
        return <Navigate to="/login" />;
    }
    return children;
}
