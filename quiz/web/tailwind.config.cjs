/** @type {import('tailwindcss').Config} */

module.exports = {
    content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
    theme: {
        colors: {
            primary: "#4459a9",
        },
        extend: {},
    },
    plugins: [
        {
            tailwindcss: { config: "./tailwindcss-config.js" },
        },
    ],
};
