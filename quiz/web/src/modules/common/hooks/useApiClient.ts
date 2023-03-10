import axios, { AxiosInstance, CreateAxiosDefaults } from "axios";
import useJwtToken from "modules/common/hooks/useJwtToken";

const isoDateFormat = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d*)?$/;

function isIsoDateString(value: unknown): boolean {
    return !!value && typeof value === "string" && isoDateFormat.test(value);
}

/**
 * Converts in place ISO datetime strings into a Date objects.
 */
function handleDates(body: Record<string, unknown> | null | undefined | string | number | boolean) {
    if (body === null || body === undefined || typeof body !== "object") {
        return;
    }

    for (const key of Object.keys(body)) {
        const value = body[key];
        if (isIsoDateString(value)) {
            body[key] = new Date(value as string);
        } else if (typeof value === "object") {
            handleDates(value as Record<string, unknown>);
        }
    }
}

/**
 * Hook allowing access to a better Axios, which:
 * - Fills Authorization header with Bearer token, if no Authorization header was provided.
 * - Parses all ISO datetime objects found in response to instance of Date.
 * */
export default function useApiClient(): AxiosInstance {
    const [token] = useJwtToken();
    const client = axios.create({} satisfies CreateAxiosDefaults);

    client.interceptors.response.use((originalResponse) => {
        handleDates(originalResponse.data);
        return originalResponse;
    });

    client.interceptors.request.use((originalRequest) => {
        originalRequest.headers = originalRequest.headers || {};
        originalRequest.headers.Authorization = originalRequest.headers.Authorization || `Bearer ${token}`;
        return originalRequest;
    });

    return client;
}
