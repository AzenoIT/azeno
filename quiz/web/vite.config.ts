import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import eslint from "vite-eslint-plugin";
import tsconfigPaths from "vite-tsconfig-paths";

export default defineConfig({
    server: {
        port: parseInt(process.env.VITE_PORT),
        host: "0.0.0.0",
    },
    plugins: [
        react(),
        tsconfigPaths(),
        { ...eslint({ failOnError: true, failOnWarning: false }), apply: "build" },
        { ...eslint({ failOnError: false, failOnWarning: false, fix: true }), apply: "serve", enforce: "post" },
    ],
});
