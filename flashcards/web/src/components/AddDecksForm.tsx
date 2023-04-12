import React from "react";
import { useFormik } from "formik";
import { Button, Container, Grid, InputLabel, MenuItem, Select, TextField, Typography } from "@mui/material";
import * as Yup from "yup";

function AddDecksForm() {
    const formik = useFormik({
        initialValues: {
            tagName: "",
            author: "",
            selectTag: "",
            selectCategory: "",
            selectAvailability: "",
            price: "",
        },
        onSubmit: (values) => {
            alert(JSON.stringify(values, null, 2));
        },
        validationSchema: Yup.object({
            tagName: Yup.string().min(2, "Too Short!").max(20, "Too Long!").required("Required!"),
            author: Yup.string().min(2, "Too Short!").max(20, "Too Long!").required("Required!"),
            price: Yup.number().integer().typeError("Must be a number"),
            selectTag: Yup.string().required("Required!"),
            selectCategory: Yup.string().required("Required!"),
            selectAvailability: Yup.string().required("Required!"),
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
                        <Select fullWidth labelId="select-tag-label" id="selectTag" onChange={formik.handleChange}>
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
                            onChange={formik.handleChange}
                        >
                            <MenuItem value="Test">Test</MenuItem>
                            <MenuItem value="Test2">Test2</MenuItem>
                            <MenuItem value="Test3">Test3</MenuItem>
                        </Select>
                        {formik.errors.selectCategory && (
                            <div className="text-red-600">{formik.errors.selectCategory}</div>
                        )}
                    </Grid>
                    <Grid item xs={12} marginBottom={2}>
                        <InputLabel id="select-availability-label">Select availability</InputLabel>
                        <Select
                            fullWidth
                            labelId="select-availability-label"
                            id="selectAvailability"
                            onChange={formik.handleChange}
                        >
                            <MenuItem value="Private">Private</MenuItem>
                            <MenuItem value="Public">Public</MenuItem>
                        </Select>
                        {formik.errors.selectAvailability && (
                            <div className="text-red-600">{formik.errors.selectAvailability}</div>
                        )}
                    </Grid>
                    <Grid item xs={12}>
                        <TextField
                            fullWidth
                            name="price"
                            label="If public, enter your price"
                            onChange={formik.handleChange}
                            value={formik.values.price}
                        />
                        {formik.errors.price && <div className="text-red-600">{formik.errors.price}</div>}
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
