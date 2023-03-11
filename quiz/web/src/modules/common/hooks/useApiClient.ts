import axios, { AxiosInstance, CreateAxiosDefaults } from "axios";
import useAuthToken from "modules/common/AuthToken/useAuthToken";

/**
 * Hook allowing access to a better Axios, which:
 * - Fills Authorization header with Bearer token, if no Authorization header was provided.
 * - Attempts to refresh access token if response status was 403 and repeats request.
 * - TODO parses all ISO date strings to Date objects.
 * */
export default function useApiClient(): AxiosInstance {
    const { accessToken, refreshAccessToken } = useAuthToken();
    const client = axios.create({} satisfies CreateAxiosDefaults);

    client.interceptors.request.use((config) => {
        const newConfig = { ...config };
        newConfig.headers = newConfig.headers || {};
        newConfig.headers.Authorization = newConfig.headers.Authorization || `Bearer ${accessToken}`;
        return newConfig;
    });

    client.interceptors.response.use(
        (response) => response,
        async (error) => {
            const originalRequest = error.config;
            if (error.response.status === 403 && !originalRequest._retry) {
                originalRequest._retry = true;
                originalRequest.headers.Authorization = `Bearer ${await refreshAccessToken()}`;
                return client(originalRequest);
            }
            return Promise.reject(error);
        }
    );

    return client;
}
