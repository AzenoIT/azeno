import axios, { AxiosError, AxiosResponse } from "axios";
import { player } from "modules/common/api_urls";
import { AnonymousUserData } from "modules/common/Auth/types";

/**
 * Function invoked to register a new anonymous player, a player which is not associated with a user.
 */
async function registerAnonymousUser(username: string): Promise<AnonymousUserData> {
    let response: AxiosResponse<AnonymousUserData>;
    try {
        response = await axios.post(player.register, { username });
    } catch (error) {
        if (error instanceof AxiosError && error.response?.status === 406) {
            return Promise.reject(new Error(error.response.data?.message));
        }
        return Promise.reject(new Error("Unexpected error has occurred."));
    }
    return response.data;
}

export { registerAnonymousUser };
