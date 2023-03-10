import { useQuery, UseQueryResult } from "@tanstack/react-query";
import axios from "axios";

interface CatFact {
    fact: string;
    length: number;
}

async function fetchCatFact(): Promise<CatFact> {
    const response = await axios.get("https://catfact.ninja/fact");
    return response.data;
}

export default function useCatFact(): UseQueryResult<CatFact> {
    return useQuery({
        queryKey: ["catFact"],
        queryFn: fetchCatFact,
    });
}
