import { describe, it } from "vitest";
import { screen, render } from "@testing-library/react";
import { ErrorBoundary } from "modules/common/components";

describe("ErrorBoundary", () => {
    it("Displays error message after catching error", () => {
        const ThrowError = () => {
            throw new Error("Random Error");
        };

        render(
            <ErrorBoundary>
                <ThrowError />
            </ErrorBoundary>
        );

        expect(screen.getByRole("heading", { name: "Sorry" })).toBeInTheDocument();
        expect(screen.getByText("Something went wrong, please try again")).toBeInTheDocument();
    });
});
