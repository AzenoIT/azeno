import axios, { AxiosError, AxiosResponse } from "axios";
import { player, token } from "modules/common/apiUrls";
import { AnonymousUserData } from "modules/common/Auth/types";
import { CreateAuthorizationTokenResponse } from "modules/common/types";

/**
 * Function invoked to register a new anonymous player, a player which is not associated with a user.
 */
async function registerAnonymousPlayer(username: string): Promise<AnonymousUserData> {
    let response: AxiosResponse<AnonymousUserData>;
    try {
        response = await axios.post(player.register(), { username });
    } catch (error) {
        if (error instanceof AxiosError && error.response?.status === 406) {
            return Promise.reject(new Error(error.response.data.message));
        }
        return Promise.reject(new Error("Unexpected error has occurred."));
    }
    return response.data;
}

/**
 * Function invoked to log in an anonymous player.
 */
async function loginAnonymousPlayer(id: string): Promise<CreateAuthorizationTokenResponse> {
    let response: AxiosResponse<CreateAuthorizationTokenResponse>;
    try {
        response = await axios.post(token.create(), { id });
    } catch (error) {
        if (error instanceof AxiosError && error.response?.status === 401) {
            return Promise.reject(new Error(error.response.data.message));
        }
        return Promise.reject(new Error("Unexpected error has occurred."));
    }
    return response.data;
}

async function refreshAccessToken(refreshToken: string): Promise<CreateAuthorizationTokenResponse> {
    let response: AxiosResponse<CreateAuthorizationTokenResponse>;
    try {
        response = await axios.post(token.refresh(), { refresh_token: refreshToken });
    } catch (error) {
        if (error instanceof AxiosError && error.response?.status === 401) {
            return Promise.reject(new Error(error.response.data.message));
        }
        return Promise.reject(new Error("Unexpected error has occurred."));
    }
    return response.data;
}

export { refreshAccessToken, registerAnonymousPlayer, loginAnonymousPlayer };
