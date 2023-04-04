/** @type {import('tailwindcss').Config} */

module.exports = {
    content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
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
            },
        },
    },
    plugins: [],
};
