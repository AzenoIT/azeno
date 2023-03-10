import { useQuery, UseQueryResult } from "@tanstack/react-query";
import { AxiosInstance } from "axios";
import { useApiClient } from "modules/common/hooks";

interface CatFact {
    fact: string;
    length: number;
}

async function fetchCatFact(axios: AxiosInstance): Promise<CatFact> {
    const response = await axios.get("https://catfact.ninja/fact");
    return response.data;
}

export default function useCatFact(): UseQueryResult<CatFact> {
    const axios = useApiClient();
    return useQuery({
        queryKey: ["catFact"],
        queryFn: () => fetchCatFact(axios),
    });
}
