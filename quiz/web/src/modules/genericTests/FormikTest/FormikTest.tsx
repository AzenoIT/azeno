import { useState } from "react";
import { useFormik } from "formik";
import * as yup from "yup";

function FormikTest() {
    const [message, setMessage] = useState("");
    const [submitted, setSubmitted] = useState(false);

    const formik = useFormik({
        initialValues: {
            email: "",
            name: "",
            message: "",
        },
        onSubmit: () => {
            setMessage("Form submitted");
            setSubmitted(true);
        },
        validationSchema: yup.object({
            name: yup.string().trim().required("Name is required"),
            email: yup.string().email("Must be a valid email").required("Email is required"),
            message: yup.string().trim().required("Message is required"),
        }),
    });

    return (
        <div className="vh-100 flex flex-col justify-center items-center">
            <div
                hidden={!submitted}
                className="relative px-3 py-3 mb-4 border rounded bg-blue-200 border-blue-300 text-blue-800"
                role="alert"
            >
                {message}
            </div>

            <form className="w-1/2" onSubmit={formik.handleSubmit}>
                <div className="mb-3">
                    <label htmlFor="name" className="form-label">
                        Name
                    </label>
                    <input
                        type="text"
                        id="name"
                        name="name"
                        className="block appearance-none w-full py-1 px-2 mb-1 text-base leading-normal bg-white text-gray-800 border border-gray-200 rounded"
                        placeholder="John Doe"
                        value={formik.values.name}
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                    />
                    {formik.errors.name && <div className="text-red-600">{formik.errors.name}</div>}
                </div>

                <div className="mb-3">
                    <label htmlFor="email" className="form-label">
                        Email
                    </label>

                    <input
                        type="email"
                        id="email"
                        name="email"
                        className="block appearance-none w-full py-1 px-2 mb-1 text-base leading-normal bg-white text-gray-800 border border-gray-200 rounded"
                        placeholder="john@example.com"
                        value={formik.values.email}
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                    />
                    {formik.errors.email && <div className="text-red-600">{formik.errors.email}</div>}
                </div>

                <div className="mb-3">
                    <label htmlFor="message" className="form-label">
                        Message
                    </label>

                    <textarea
                        id="message"
                        name="message"
                        className="block appearance-none w-full py-1 px-2 mb-1 text-base leading-normal bg-white text-gray-800 border border-gray-200 rounded"
                        placeholder="Your message ..."
                        value={formik.values.message}
                        onChange={formik.handleChange}
                        onBlur={formik.handleBlur}
                    />
                    {formik.errors.message && <div className="text-red-600">{formik.errors.message}</div>}
                </div>

                <button
                    type="submit"
                    className="inline-block align-middle text-center select-none border font-normal whitespace-no-wrap rounded py-1 px-3 leading-normal no-underline bg-blue-600 text-white hover:bg-blue-600"
                >
                    Send
                </button>
            </form>
        </div>
    );
}

export default FormikTest;
