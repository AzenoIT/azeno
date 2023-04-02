const baseUrl = "/api/v1";
const player = {
    register: () => `${baseUrl}/player/register/`,
    username: () => `${baseUrl}/player/username/`,
} as const;

const token = {
    create: () => `${baseUrl}/token/`,
    refresh: () => `${baseUrl}/refresh/`,
} as const;

export { baseUrl, player, token };
