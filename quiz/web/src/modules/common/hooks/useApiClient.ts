import axios, { AxiosInstance, CreateAxiosDefaults } from "axios";
import useJwtToken from "modules/common/hooks/useJwtToken";

/**
 * Hook allowing access to a better Axios, which:
 * - Fills Authorization header with Bearer token, if no Authorization header was provided.
 * */
export default function useApiClient(): AxiosInstance {
    const [token] = useJwtToken();
    const client = axios.create({} satisfies CreateAxiosDefaults);

    client.interceptors.request.use((originalRequest) => {
        const newRequest = { ...originalRequest };
        newRequest.headers = originalRequest.headers || {};
        newRequest.headers.Authorization = originalRequest.headers.Authorization || `Bearer ${token}`;
        return newRequest;
    });

    return client;
}
