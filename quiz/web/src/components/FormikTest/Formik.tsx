import { Formik, Form, useField } from "formik";
import * as Yup from "yup";
import styled from "styled-components";
import "./styles.css";
import "./styles-custom.css";

const MyTextInput = ({ label, ...props }) => {
    // useField() returns [formik.getFieldProps(), formik.getFieldMeta()]
    // which we can spread on <input> and alse replace ErrorMessage entirely.
    const [field, meta] = useField(props);
    return (
        <>
            <label htmlFor={props.id || props.name}>{label}</label>
            <input className="text-input" {...field} {...props} />
            {meta.touched && meta.error ? (
                <div className="error">{meta.error}</div>
            ) : null}
        </>
    );
};

const MyCheckbox = ({ children, ...props }) => {
    const [field, meta] = useField({ ...props, type: "checkbox" });
    return (
        <>
            <label className="checkbox">
                <input {...field} {...props} type="checkbox" />
                {children}
            </label>
            {meta.touched && meta.error ? (
                <div className="error">{meta.error}</div>
            ) : null}
        </>
    );
};

// Styled components ....
const StyledSelect = styled.select`
  color: var(--blue);
`;

const StyledErrorMessage = styled.div`
  font-size: 12px;
  color: var(--red-600);
  width: 400px;
  margin-top: 0.25rem;
  &:before {
    content: "❌ ";
    font-size: 10px;
  }
  @media (prefers-color-scheme: dark) {
    color: var(--red-300);
  }
`;

const StyledLabel = styled.label`
  margin-top: 1rem;
`;

const MySelect = ({ label, ...props }) => {
    // useField() returns [formik.getFieldProps(), formik.getFieldMeta()]
    // which we can spread on <input> and alse replace ErrorMessage entirely.
    const [field, meta] = useField(props);
    return (
        <>
            <StyledLabel htmlFor={props.id || props.name}>{label}</StyledLabel>
            <StyledSelect {...field} {...props} />
            {meta.touched && meta.error ? (
                <StyledErrorMessage>{meta.error}</StyledErrorMessage>
            ) : null}
        </>
    );
};

// And now we can use these
const SignupForm = () => {
    return (
        <>
            <h1>Subscribe!</h1>
            <Formik
                initialValues={{
                    firstName: "",
                    lastName: "",
                    email: "",
                    acceptedTerms: false, // added for our checkbox
                    jobType: "" // added for our select
                }}
                validationSchema={Yup.object({
                    firstName: Yup.string()
                        .max(15, "Must be 15 characters or less")
                        .required("Required"),
                    lastName: Yup.string()
                        .max(20, "Must be 20 characters or less")
                        .required("Required"),
                    email: Yup.string()
                        .email("Invalid email addresss`")
                        .required("Required"),
                    acceptedTerms: Yup.boolean()
                        .required("Required")
                        .oneOf([true], "You must accept the terms and conditions."),
                    jobType: Yup.string()
                        // specify the set of valid values for job type
                        // @see http://bit.ly/yup-mixed-oneOf
                        .oneOf(
                            ["designer", "development", "product", "other"],
                            "Invalid Job Type"
                        )
                        .required("Required")
                })}
                onSubmit={async (values, { setSubmitting }) => {
                    await new Promise(r => setTimeout(r, 500));
                    setSubmitting(false);
                }}
            >
                <Form>
                    <MyTextInput
                        label="First Name"
                        name="firstName"
                        type="text"
                        placeholder="Jane"
                    />
                    <MyTextInput
                        label="Last Name"
                        name="lastName"
                        type="text"
                        placeholder="Doe"
                    />
                    <MyTextInput
                        label="Email Address"
                        name="email"
                        type="email"
                        placeholder="jane@formik.com"
                    />
                    <MySelect label="Job Type" name="jobType">
                        <option value="">Select a job type</option>
                        <option value="designer">Designer</option>
                        <option value="development">Developer</option>
                        <option value="product">Product Manager</option>
                        <option value="other">Other</option>
                    </MySelect>
                    <MyCheckbox name="acceptedTerms">
                        I accept the terms and conditions
                    </MyCheckbox>

                    <button type="submit">Submit</button>
                </Form>
            </Formik>
        </>
    );
};

export default SignupForm as Formik;
