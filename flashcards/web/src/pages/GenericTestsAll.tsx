import React from "react";
import FormikTest from "modules/genericTests/FormikTest/FormikTest";
import TailwindTest from "modules/genericTests/TailwindTest/TailwindTest";
import FakerTest from "modules/genericTests/FakerTest/FakerTest";
import MaterialUITest from "modules/genericTests/MaterialUITest/MaterialUITest";

function GenericTestsAll() {
    return (
        <>
            <h1>Tests</h1>
            <FakerTest />
            <TailwindTest />
            <FormikTest />
            <MaterialUITest />
        </>
    );
}

export default GenericTestsAll;
