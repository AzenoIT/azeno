import React from "react";

import { render } from "@testing-library/react-native";
// eslint-disable-next-line import/no-extraneous-dependencies
import { expect } from "vitest";
import App from "./App";

test("should render the button", async () => {
    const container = render(<App />);

    const loginBtn = await container.findByTestId("login__btn");

    expect(loginBtn.text).toBe("Go to Login Screen");

    container.unmount();
});
