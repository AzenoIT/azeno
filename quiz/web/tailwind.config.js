/** @type {import("tailwindcss").Config} */

import config from "@azeno/bank/tailwind.config.cjs";

export default {
    content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}", "../../node_modules/@azeno/bank/**/*.{js,ts,jsx,tsx}"],
    theme: {
        extend: {
            container: {
                center: true,
            },
            colors: {
                ...config.theme.extend.colors,
                primary40: "#4459a9",
                primary70: "#92A7FD",
                primary90: "#DDE1FF",
                secondary90: "#DBE1FF",
            },
        },
    },
    plugins: [],
};
