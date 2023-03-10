import useLocalStorage from "modules/common/hooks/useLocalStorage";

/**
 * Hook allowing access to JWT token stored in localstorage.
 * TODO Add refresh of invalid tokens.
 * */
export default function useJwtToken(): [string, (newToken: string) => void] {
    const [token, setToken] = useLocalStorage("JwtToken", "");
    return [token, setToken];
}
