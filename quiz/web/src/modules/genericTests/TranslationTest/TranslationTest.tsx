import { useTranslation } from "react-i18next";

function translationTest() {
    const { t, i18n } = useTranslation();
    const langs = {
        en: { nativeName: "English" },
        de: { nativeName: "Deutsch" },
        pl: { nativeName: "Polish" },
    };

    return (
        <>
            <h2>{`${t("Learn")} React`}</h2>
            <h2>{`${t("Hello World")}!`}</h2>

            <div>
                {Object.keys(langs).map((lang) => (
                    <button
                        type="submit"
                        key={lang}
                        onClick={() => i18n.changeLanguage(lang)}
                        disabled={i18n.resolvedLanguage === lang}
                    >
                        {langs[lang].nativeName}
                    </button>
                ))}
            </div>
        </>
    );
}

export default translationTest;
