import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import useLocalStorage from "modules/common/AuthToken/useLocalStorage/useLocalStorage";
import { beforeEach, describe, expect } from "vitest";

describe("useLocalStorage", () => {
    function UseLocalStorageConsumer() {
        const [value, setValue] = useLocalStorage("RandomKey", "DefaultValue");

        return (
            <div>
                <h1>{value}</h1>
                <button type="button" onClick={() => setValue("42")}>
                    setValue
                </button>
            </div>
        );
    }

    beforeEach(() => {
        localStorage.removeItem("RandomKey");
        return () => localStorage.removeItem("RandomKey");
    });

    test("returns default value when no value was found in localStorage", () => {
        render(<UseLocalStorageConsumer />);

        expect(screen.getByRole("heading").textContent).toBe("DefaultValue");
        expect(JSON.parse(localStorage.getItem("RandomKey") || "")).toBe("DefaultValue");
    });

    test("returns value from localStorage when exists", () => {
        localStorage.setItem("RandomKey", JSON.stringify("NonDefaultValue"));
        render(<UseLocalStorageConsumer />);

        expect(screen.getByRole("heading").textContent).toBe("NonDefaultValue");
    });

    test("updates value in localStorage", async () => {
        render(<UseLocalStorageConsumer />);

        expect(screen.getByRole("heading").textContent).toBe("DefaultValue");
        await userEvent.click(screen.getByRole("button"));

        await waitFor(() => expect(screen.getByRole("heading").textContent).toBe("42"));
        expect(JSON.parse(localStorage.getItem("RandomKey") || "")).toBe("42");
    });
});
