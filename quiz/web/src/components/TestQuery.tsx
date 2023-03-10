import { useQuery, UseQueryResult } from "@tanstack/react-query";
import axios from "axios";

export default function TestQuery() {
    const { data, isLoading } = useCatFact();

    if (isLoading || !data) {
        return <h2>Loading</h2>;
    }
    return (
        <div>
            <h2>{data.fact}</h2>
        </div>
    );
}

interface CatFact {
    fact: string;
    length: number;
}

async function fetchCatFact(): Promise<CatFact> {
    const response = await axios.get("https://catfact.ninja/fact");
    return response.data;
}

function useCatFact(): UseQueryResult<CatFact> {
    return useQuery({
        queryKey: ["catFact"],
        queryFn: fetchCatFact,
    });
}
