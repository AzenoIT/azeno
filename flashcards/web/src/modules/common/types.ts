export interface CreateAuthorizationTokenResponse {
    access_token: string;
    expires_at: string;
    refresh_expires_at: string;
    refresh_token: string;
    token_type: "Bearer";
    scope: string[];
    session_state: string;
}
