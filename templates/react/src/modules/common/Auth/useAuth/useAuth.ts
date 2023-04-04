import { AnonymousUserData, RegisteredUserData } from "modules/common/Auth/types";
import * as utils from "modules/common/Auth/useAuth/utils";
import useLocalStorage from "modules/common/Auth/useLocalStorage";
import { CreateAuthorizationTokenResponse } from "modules/common/types";
import { useCallback } from "react";

type AuthData =
    | { readonly userType: "registered"; readonly data: RegisteredUserData }
    | { readonly userType: "anonymous"; readonly data: AnonymousUserData }
    | { readonly userType: null };

interface UseAuth {
    readonly accessToken: string;
    readonly refreshToken: string;
    isTokenValid: () => boolean;
    isRefreshTokenValid: () => boolean;
    refreshAccessToken: () => Promise<string>;
    getUserDetail: () => AnonymousUserData | RegisteredUserData | null;
    loginAnonymous: () => Promise<void>;
    register: (username: string) => Promise<AnonymousUserData>;
}

/**
 * Hook allowing access to JWT token stored in localstorage.
 * Allows for setting tokens as well as refreshing accessToken using refreshToken.
 * */
export default function useAuth(): UseAuth {
    const [authData, setAuthData] = useLocalStorage<AuthData>("userData", { userType: null });

    const [{ accessToken, refreshToken, expiresAt, refreshExpiresAt }, setTokens] = useLocalStorage("authToken", {
        accessToken: "",
        expiresAt: "1970-01-01T00:00:00.000Z",
        refreshExpiresAt: "1970-01-01T00:00:00.000Z",
        refreshToken: "",
    });

    const isRefreshTokenValid = useCallback(() => {
        return new Date(refreshExpiresAt) > new Date() && refreshToken !== "";
    }, [refreshExpiresAt, refreshToken]);

    const isTokenValid = useCallback(() => {
        return (new Date(expiresAt) > new Date() && accessToken !== "") || isRefreshTokenValid();
    }, [expiresAt, isRefreshTokenValid, accessToken]);

    const refreshAccessToken = useCallback(async (): Promise<string> => {
        const tokenData: CreateAuthorizationTokenResponse = await utils.refreshAccessToken(refreshToken);
        setTokens({
            accessToken: tokenData.access_token,
            refreshToken: tokenData.refresh_token,
            expiresAt: tokenData.expires_at,
            refreshExpiresAt: tokenData.refresh_expires_at,
        });
        return Promise.resolve(tokenData.access_token);
    }, [refreshToken, setTokens]);

    const getUserDetail = useCallback(() => {
        if (authData.userType === null) return null;
        return authData.data;
    }, [authData]);

    const loginAnonymous = useCallback(async () => {
        if (authData.userType === "anonymous") {
            const tokenData: CreateAuthorizationTokenResponse = await utils.loginAnonymousPlayer(authData.data.id);
            setTokens({
                accessToken: tokenData.access_token,
                refreshToken: tokenData.refresh_token,
                expiresAt: tokenData.expires_at,
                refreshExpiresAt: tokenData.refresh_expires_at,
            });
        }
    }, [setTokens, authData]);

    const register = useCallback(
        async (username: string): Promise<AnonymousUserData> => {
            const userData: AnonymousUserData = await utils.registerAnonymousPlayer(username);
            setAuthData({ userType: "anonymous", data: userData });
            const tokenData: CreateAuthorizationTokenResponse = await utils.loginAnonymousPlayer(userData.id);
            setTokens({
                accessToken: tokenData.access_token,
                refreshToken: tokenData.refresh_token,
                expiresAt: tokenData.expires_at,
                refreshExpiresAt: tokenData.refresh_expires_at,
            });
            return Promise.resolve(userData);
        },
        [setAuthData, setTokens]
    );

    return {
        accessToken,
        refreshToken,
        isTokenValid,
        isRefreshTokenValid,
        refreshAccessToken,
        getUserDetail,
        loginAnonymous,
        register,
    };
}
