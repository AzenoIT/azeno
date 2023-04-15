import React from "react";

import { render } from "@testing-library/react-native";
// eslint-disable-next-line import/no-extraneous-dependencies
import { expect } from "vitest";
import Login from "Login";

describe("test", () => {
    test("should display no errors before the user started typing", async () => {
        const container = render(<Login />);
        const yupError = await container.findByTestId("yup__error");

        expect(yupError.text).toBe("");

        container.unmount();
    });
});
