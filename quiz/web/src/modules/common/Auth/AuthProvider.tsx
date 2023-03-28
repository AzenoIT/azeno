import { AuthConfig } from "modules/common/Auth/types";
import { createContext, useContext } from "react";

const AuthContext = createContext<AuthConfig>({ loginEndpoint: "", refreshEndpoint: "" });

export function AuthProvider({ config, children }: { config: AuthConfig; children: JSX.Element }) {
    return <AuthContext.Provider value={config}>{children}</AuthContext.Provider>;
}

export function useAuthConfig() {
    return useContext(AuthContext);
}
