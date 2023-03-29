import axios, { AxiosResponse } from "axios";
import { player } from "modules/common/api_urls";
import { AnonymousUserData } from "modules/common/Auth/types";

/**
 * Function invoked to register a new anonymous player, a player which is not associated with a user.
 */
async function registerAnonymousUser(username: string) {
    let response: AxiosResponse<AnonymousUserData>;
    try {
        response = await axios.post(player.register, { username });
    } catch (error) {}

    return response.data;
}

export { registerAnonymousUser };
