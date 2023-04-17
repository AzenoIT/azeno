// @ts-nocheck

import React from "react";
import { useFormik } from "formik";
import {
    Button,
    Checkbox,
    Container,
    FormControlLabel,
    Grid,
    InputLabel,
    MenuItem,
    Select,
    TextField,
    Typography,
} from "@mui/material";
import * as Yup from "yup";

function AddDecksForm() {
    const formik = useFormik({
        validateOnChange: false,
        initialValues: {
            tagName: "",
            author: "",
            selectTag: "",
            selectCategory: "",
            selectAvailability: "",
            price: "",
            checkboxPublic: false,
            checkboxPrice: false,
        },
        onSubmit: (values) => {
            alert(JSON.stringify(values, null, 2));
        },
        validationSchema: Yup.object().shape({
            tagName: Yup.string().min(2, "Too Short!").max(20, "Too Long!").required("Required!"),
            author: Yup.string().min(2, "Too Short!").max(20, "Too Long!").required("Required!"),
            checkboxPrice: Yup.boolean(),
            checkboxPublic: Yup.boolean(),
            price: Yup.number().when("checkboxPrice", {
                is: true,
                then: Yup.number().required("Required!"),
            }),
            selectTag: Yup.string().required("Required!"),
            selectCategory: Yup.string().required("Required!"),
        }),
    });
    return (
        <form onSubmit={formik.handleSubmit}>
            <Container maxWidth="md">
                <Grid container>
                    <Grid item xs={12}>
                        <Typography>Add decks form</Typography>
                    </Grid>
                    <Grid item xs={12} marginBottom={2}>
                        <TextField
                            fullWidth
                            name="tagName"
                            label="Tag name"
                            onChange={formik.handleChange}
                            value={formik.values.tagName}
                        />
                        {formik.errors.tagName && <div className="text-red-600">{formik.errors.tagName}</div>}
                    </Grid>
                    <Grid item xs={12} marginBottom={2}>
                        <TextField
                            fullWidth
                            name="author"
                            label="Author"
                            onChange={formik.handleChange}
                            value={formik.values.author}
                        />
                        {formik.errors.author && <div className="text-red-600">{formik.errors.author}</div>}
                    </Grid>
                    <Grid item xs={12} marginBottom={2}>
                        <InputLabel id="select-tag-label">Select Tag</InputLabel>
                        <Select
                            fullWidth
                            labelId="select-tag-label"
                            id="selectTag"
                            name="selectTag"
                            onChange={formik.handleChange}
                            value={formik.values.selectTag}
                        >
                            <MenuItem value="Test">Test</MenuItem>
                            <MenuItem value="Test2">Test2</MenuItem>
                            <MenuItem value="Test3">Test3</MenuItem>
                        </Select>
                        {formik.errors.selectTag && <div className="text-red-600">{formik.errors.selectTag}</div>}
                    </Grid>
                    <Grid item xs={12} marginBottom={2}>
                        <InputLabel id="select-a-category-label">Select a category</InputLabel>
                        <Select
                            fullWidth
                            labelId="select-a-category-label"
                            id="selectCategory"
                            name="selectCategory"
                            onChange={formik.handleChange}
                            value={formik.values.selectCategory}
                        >
                            <MenuItem value="Test">Test</MenuItem>
                            <MenuItem value="Test2">Test2</MenuItem>
                            <MenuItem value="Test3">Test3</MenuItem>
                        </Select>
                        {formik.errors.selectCategory && (
                            <div className="text-red-600">{formik.errors.selectCategory}</div>
                        )}
                    </Grid>
                    <Grid item xs={12}>
                        <FormControlLabel
                            control={
                                <Checkbox
                                    checked={formik.values.checkboxPublic}
                                    onChange={formik.handleChange}
                                    name="checkboxPublic"
                                />
                            }
                            label="Public"
                        />
                        {formik.values.checkboxPublic && (
                            <FormControlLabel
                                control={
                                    <Checkbox
                                        checked={formik.values.checkboxPrice}
                                        onChange={formik.handleChange}
                                        name="checkboxPrice"
                                    />
                                }
                                label="For sale"
                            />
                        )}
                        {formik.values.checkboxPrice && (
                            <>
                                <TextField
                                    fullWidth
                                    name="price"
                                    label="Enter your price"
                                    onChange={formik.handleChange}
                                    value={formik.values.price}
                                />
                                {formik.errors.price && <div className="text-red-600">{formik.errors.price}</div>}
                            </>
                        )}
                    </Grid>
                    <Grid margin={5}>
                        <Button type="submit" variant="contained">
                            Submit
                        </Button>
                    </Grid>
                </Grid>
            </Container>
        </form>
    );
}

export default AddDecksForm;
