import { AuthConfig } from "modules/common/AuthToken/types";
import { createContext, useContext } from "react";

const AuthTokenContext = createContext<AuthConfig>({ loginEndpoint: "", refreshEndpoint: "" });

export function AuthTokenProvider({ config, children }: { config: AuthConfig; children: JSX.Element }) {
    return <AuthTokenContext.Provider value={config}>{children}</AuthTokenContext.Provider>;
}

export function useAuthTokenConfig() {
    return useContext(AuthTokenContext);
}
