/** @type {import('tailwindcss').Config} */

module.exports = {
    content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}", "../../node_modules/@azeno/bank/**/*.{js,ts,jsx,tsx}"],
    important: "#root",
    theme: {
        extend: {
            container: {
                center: true,
            },
            colors: {
                primary40: "#4459a9",
                primary70: "#92A7FD",
                primary90: "#DDE1FF",
                secondary90: "#DBE1FF",
                primary: "#4459A9",
                secondary: "#DBE1FF",
                success: "#65A014",
                warning: "#FDBC11",
                error: "#BA1A1A",
            },
        },
    },
    plugins: [],
};
