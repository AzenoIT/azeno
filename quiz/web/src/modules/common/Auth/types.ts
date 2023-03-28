export interface AuthConfig {
    loginEndpoint: string;
    refreshEndpoint: string;
}

export interface AnonymousUserData {
    id: string;
    username: string;
}

export interface RegisteredUserData extends AnonymousUserData {}
