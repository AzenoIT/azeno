import { defineConfig } from "cypress";

export default defineConfig({
    fixturesFolder: false,
    e2e: {
        setupNodeEvents(on, config) {},
        supportFile: false,
        baseUrl: "http://localhost:19006",
    },
});
