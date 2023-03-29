import axios, { AxiosResponse } from "axios";
import { useAuthConfig } from "modules/common/Auth/AuthProvider";
import { AnonymousUserData, RegisteredUserData } from "modules/common/Auth/types";
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
    refreshAccessToken: () => Promise<string>;
    isTokenValid: () => boolean;
    isRefreshTokenValid: () => boolean;
    login: (username: string, password: string) => Promise<string>;
    getUserDetail: () => AnonymousUserData | RegisteredUserData | null;
    setUserDetail: (authData: AuthData) => void;
}

/**
 * Hook allowing access to JWT token stored in localstorage.
 * Allows for setting tokens as well as refreshing accessToken using refreshToken.
 * */

export default function useAuth(): UseAuth {
    const config = useAuthConfig();
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

    const refreshAccessToken = useCallback(async () => {
        let response: AxiosResponse<CreateAuthorizationTokenResponse>;
        try {
            response = await axios.post<CreateAuthorizationTokenResponse>(config.refreshEndpoint, {
                refresh_token: refreshToken,
            });
        } catch (error) {
            return Promise.reject(new Error("Token refresh failed."));
        }

        setTokens({
            accessToken: response.data.access_token,
            refreshToken: response.data.refresh_token,
            expiresAt: response.data.expires_at,
            refreshExpiresAt: response.data.refresh_expires_at,
        });
        return Promise.resolve(response.data.access_token);
    }, [config, refreshToken, setTokens]);

    // TODO update following methods
    // TODO 1. register -> so that a user can register an anonymous user account
    // TODO 2. login -> support for anonymous user
    // TODO 3.
    const getUserDetail = useCallback(() => {
        if (authData.userType === null) return null;
        return authData.data;
    }, [authData]);

    const setUserDetail = useCallback(
        (value: AuthData) => {
            setAuthData(value);
        },
        [setAuthData]
    );

    const login = useCallback(
        async (username: string, password: string) => {
            let response: AxiosResponse<CreateAuthorizationTokenResponse>;
            try {
                response = await axios.post<CreateAuthorizationTokenResponse>(config.loginEndpoint, {
                    username,
                    password,
                });
            } catch (err) {
                return Promise.reject(err);
            }

            setTokens({
                accessToken: response.data.access_token,
                refreshToken: response.data.refresh_token,
                expiresAt: response.data.expires_at,
                refreshExpiresAt: response.data.refresh_expires_at,
            });
            return Promise.resolve("Login successful");
        },
        [setTokens, config.loginEndpoint]
    );

    return {
        accessToken,
        refreshToken,
        refreshAccessToken,
        isTokenValid,
        isRefreshTokenValid,
        login,
        getUserDetail,
        setUserDetail,
    };
}
