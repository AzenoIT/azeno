const player = {
    register: "/player/register/",
    username: "/player/username/",
} as const;

const token = {
    create: "/token/",
    refresh: "/refresh/",
} as const;

export { player, token };
