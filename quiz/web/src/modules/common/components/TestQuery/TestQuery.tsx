import useCatFact from "modules/common/components/TestQuery/api";

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
