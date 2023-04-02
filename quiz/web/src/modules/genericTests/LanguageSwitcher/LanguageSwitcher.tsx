import { useTranslation } from "react-i18next";

const langs = {
    en: { nativeName: "English" },
    de: { nativeName: "Deutsch" },
    pl: { nativeName: "Polish" },
};

function LanguageSwitcher() {
    const { i18n } = useTranslation();

    return (
        <div>
            {Object.keys(langs).map((lang: keyof typeof langs) => (
                <button
                    type="submit"
                    key={lang}
                    onClick={() => i18n.changeLanguage(lang)}
                    disabled={i18n.resolvedLanguage === lang}
                    className="border-2 mx-1 p-1 pointer"
                >
                    {langs[lang].nativeName}
                </button>
            ))}
        </div>
    );
}

export default LanguageSwitcher;
