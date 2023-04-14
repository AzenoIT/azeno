import react from "@vitejs/plugin-react-swc";
import { defineConfig } from "vitest/config";
import eslint from "vite-eslint-plugin";
import tsconfigPaths from "vite-tsconfig-paths";

export default defineConfig({
    test: {
        globals: true,
        environment: "happy-dom",
        exclude: ["node_modules"],
        setupFiles: "src/setupTests.ts",
        coverage: {
            provider: "c8",
            lines: 80,
            functions: 80,
            branches: 80,
            statements: 80,
            all: true,
            include: ["src"],
            exclude: [
                "src/App.tsx",
                "src/main.tsx",
                "src/router.tsx",
                "src/vite-env.d.ts",
                "**/index.ts",
                "**/types.ts",
                "src/modules/common/i18nTranslation/config.ts",
                "src/modules/genericTests",
            ],
        },
    },
    server: {
        port: parseInt(process.env.VITE_PORT, 10),
        host: "0.0.0.0",
    },
    plugins: [
        react(),
        tsconfigPaths(),
        { ...eslint({ failOnError: true, failOnWarning: false }), apply: "build" },
        { ...eslint({ failOnError: false, failOnWarning: false, fix: true }), apply: "serve", enforce: "post" },
    ],
});
