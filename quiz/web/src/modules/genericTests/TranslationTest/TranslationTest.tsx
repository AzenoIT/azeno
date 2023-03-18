import { useTranslation } from "react-i18next";

function translationTest() {
    const { t } = useTranslation();

    return (
        <>
            <h2>{`${t("Learn")} React`}</h2>
            <h2>{`${t("Hello World")}!`}</h2>
        </>
    );
}

export default translationTest;
