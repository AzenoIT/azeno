// eslint-disable-next-line import/no-extraneous-dependencies
import createFetchMock from "vitest-fetch-mock";
// eslint-disable-next-line import/no-extraneous-dependencies
import { vi } from "vitest";

const fetchMock = createFetchMock(vi);
fetchMock.enableMocks();
