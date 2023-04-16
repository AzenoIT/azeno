/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
    theme: {
        extend: {
            colors: {
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
