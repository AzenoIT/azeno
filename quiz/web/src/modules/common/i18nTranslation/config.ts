import i18next from "i18next";
import { initReactI18next } from "react-i18next";
import LanguageDetector from "i18next-browser-languagedetector";
import { en, de, pl } from "./languages/index";

i18next.use(initReactI18next).use(LanguageDetector).init({
    debug: true,
    fallbackLng: "en",
    resources: {
        en,
        de,
        pl,
    },
});
