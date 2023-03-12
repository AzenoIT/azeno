// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import "@testing-library/jest-dom";

import { server } from "mocks/server";
import { beforeAll, beforeEach } from "vitest";

beforeAll(() => {
    // Server has to be globally scoped, so it can properly intercept all api calls during tests.
    server.listen({ onUnhandledRequest: "error" });
    return () => server.close();
});

beforeEach(() => {
    server.resetHandlers();
    window.location.assign("http://localhost/");
});
