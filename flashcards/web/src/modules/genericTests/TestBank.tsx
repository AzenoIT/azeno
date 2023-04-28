import { Button } from "@azeno/bank/src/components";

export default function TestBank() {
    const doNothing = () => {
        let x = 42;
        const y = x + 2;
        x = y + 1;
    };

    return (
        <Button size="lg" color="success" onClick={doNothing}>
            Hello World
        </Button>
    );
}
