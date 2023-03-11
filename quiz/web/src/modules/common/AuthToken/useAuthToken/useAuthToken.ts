import axios from "axios";
import { useAuthTokenConfig } from "modules/common/AuthToken/AuthTokenProvider";
import { AuthTokens } from "modules/common/AuthToken/types";
import useLocalStorage from "modules/common/AuthToken/useLocalStorage";
import { useCallback } from "react";

interface UseAuthToken {
    readonly accessToken: string;
    readonly refreshToken: string;
    refreshAccessToken: () => Promise<string>;
    setAccessToken: (token: string) => void;
    setRefreshToken: (token: string) => void;
    setTokens: (tokens: AuthTokens) => void;
}

/**
 * Hook allowing access to JWT token stored in localstorage.
 * Allows for setting tokens as well as refreshing accessToken using refreshToken.
 * */
export default function useAuthToken(): UseAuthToken {
    const config = useAuthTokenConfig();
    const [{ accessToken, refreshToken }, setTokens] = useLocalStorage("authToken", {
        accessToken: "",
        refreshToken: "",
    });

    const setAccessToken = useCallback(
        (token: string) => {
            setTokens((prev) => ({ ...prev, accessToken: token }));
        },
        [setTokens]
    );

    const setRefreshToken = useCallback(
        (token: string) => {
            setTokens((prev) => ({ ...prev, refreshToken: token }));
        },
        [setTokens]
    );

    const refreshAccessToken = useCallback(async () => {
        const response = await axios.post<{ access_token: string }>(
            config.tokenEndpoint,
            {
                grant_type: "refresh_token",
                refresh_token: refreshToken,
            },
            { headers: { "content-type": "application/x-www-form-urlencoded" } }
        );
        if (response.status !== 200) {
            return Promise.reject(new Error("Token refresh failed."));
        }
        setAccessToken(response.data.access_token);
        return Promise.resolve(response.data.access_token);
    }, [config, setAccessToken, refreshToken]);

    return { accessToken, refreshToken, refreshAccessToken, setAccessToken, setRefreshToken, setTokens };
}
