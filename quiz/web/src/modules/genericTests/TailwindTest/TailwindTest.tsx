import { useTranslation } from "react-i18next";

function TailwindTest() {
    const { t } = useTranslation();

    return <h1 className="text-3xl font-bold underline">{t("Hello World")}!</h1>;
}

export default TailwindTest;
