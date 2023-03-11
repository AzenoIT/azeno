import { setupServer } from "msw/node";
import { RestHandler } from "msw";

const handlers: RestHandler[] = [];

// eslint-disable-next-line import/prefer-default-export
export const server = setupServer(...handlers);
