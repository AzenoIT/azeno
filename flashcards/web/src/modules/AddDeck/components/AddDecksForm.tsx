import { ChangeEvent, useState } from "react";
import { Formik, Form, ErrorMessage, FormikHelpers } from "formik";
import * as Yup from "yup";
import { TextField, Typography, Button, Select, InputLabel, MenuItem, Checkbox, FormControlLabel } from "@mui/material";

interface FormValues {
    tagName: string;
    deckName: string;
    selectTag: string;
    selectCategory: string;
    checkboxPublic: boolean;
    checkboxForSale: boolean;
    price: number | string | boolean;
}

const validationSchema = Yup.object({
    tagName: Yup.string().min(2, "Too Short!").max(20, "Too Long!").required("Required!"),
    deckName: Yup.string().min(2, "Too Short!").max(20, "Too Long!").required("Required!"),
    selectTag: Yup.string().required("Required!"),
    selectCategory: Yup.string().required("Required!"),
    checkboxPublic: Yup.boolean(),
    checkboxForSale: Yup.boolean(),
    price: Yup.number().when("checkboxForSale", {
        is: true,
        then: Yup.number().required("Price is required!"),
        otherwise: Yup.number().nullable(),
    }),
});

const initialValues: FormValues = {
    tagName: "",
    deckName: "",
    selectTag: "",
    selectCategory: "",
    checkboxPublic: false,
    checkboxForSale: false,
    price: "",
};

function AddDecksForm() {
    const [state, setState] = useState<FormValues>(initialValues);

    const handleCheckboxPublicChange = (event: ChangeEvent<HTMLInputElement>) => {
        setState({ ...state, checkboxPublic: event.target.checked });
    };

    const handleCheckboxForSaleChange = (event: ChangeEvent<HTMLInputElement>) => {
        setState({ ...state, checkboxForSale: event.target.checked, price: event.target.checked });
    };

    const handleSubmit = (values: FormValues, actions: FormikHelpers<FormValues>) => {
        setTimeout(() => {
            alert(JSON.stringify(values, null, 2));
            actions.setSubmitting(false);
        }, 1000);
    };

    return (
        <Formik initialValues={initialValues} validationSchema={validationSchema} onSubmit={handleSubmit}>
            {({ isSubmitting }) => (
                <div className="vh-100 flex flex-col justify-center items-center">
                    <Form className="w-1/2">
                        <div className="mb-3 flex justify-center">
                            <Typography>Add decks form</Typography>
                        </div>
                        <div className="mb-3">
                            <TextField type="text" name="tagName" label="Tag name" fullWidth />
                            <ErrorMessage name="tagName" />
                        </div>

                        <div className="mb-3">
                            <TextField type="text" name="deckName" label="Deck name" fullWidth />
                            <ErrorMessage name="deckName" />
                        </div>

                        <div className="mb-3">
                            <InputLabel id="select-tag-label">Select Tag</InputLabel>
                            <Select fullWidth labelId="select-tag-label" id="selectTag" name="selectTag">
                                <MenuItem value="Test">Test</MenuItem>
                                <MenuItem value="Test2">Test2</MenuItem>
                                <MenuItem value="Test3">Test3</MenuItem>
                            </Select>
                            <ErrorMessage name="selectTag" />
                        </div>
                        <div className="mb-3">
                            <InputLabel id="select-a-category-label">Select a category</InputLabel>
                            <Select
                                fullWidth
                                labelId="select-a-category-label"
                                id="selectCategory"
                                name="selectCategory"
                            >
                                <MenuItem value="Test">Test</MenuItem>
                                <MenuItem value="Test2">Test2</MenuItem>
                                <MenuItem value="Test3">Test3</MenuItem>
                            </Select>
                            <ErrorMessage name="selectCategory" />
                        </div>

                        <div>
                            <FormControlLabel
                                control={
                                    <Checkbox checked={state.checkboxPublic} onChange={handleCheckboxPublicChange} />
                                }
                                label="Public"
                            />
                        </div>

                        <div>
                            {state.checkboxPublic && (
                                <div className="mb-3">
                                    <FormControlLabel
                                        control={
                                            <Checkbox
                                                checked={state.checkboxForSale}
                                                onChange={handleCheckboxForSaleChange}
                                            />
                                        }
                                        label="For sale"
                                    />
                                </div>
                            )}
                            {state.price && (
                                <div className="mb-3">
                                    <TextField type="text" name="price" label="Enter your price" fullWidth />
                                    <ErrorMessage name="price" />
                                </div>
                            )}
                        </div>

                        <div className="flex justify-center mb-3">
                            <Button variant="contained" type="submit" disabled={isSubmitting}>
                                Submit
                            </Button>
                        </div>
                    </Form>
                </div>
            )}
        </Formik>
    );
}

export default AddDecksForm;
