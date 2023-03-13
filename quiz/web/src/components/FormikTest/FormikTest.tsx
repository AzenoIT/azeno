import { useState } from "react";
import { useFormik } from "formik";
import * as yup from "yup";

function FormikTest({ user }) {
    const [message, setMessage] = useState("");
    const [submitted, setSubmitted] = useState(false);

    const formik = useFormik({
        initialValues: {
            email: `${user.email}`,
            name: `${user.firstName} ${user.lastName}`,
            message: "You have something to tell us?",
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
            <div className="flex flex-col w-96 my-5">
                <h2 className="text-3xl font-medium">Wielki brat Faker.js mówi:</h2>
                <p className="mb-2">
                    Your name is {user.firstName} and your last name is {user.lastName}.
                </p>
                <p className="mb-2">We know everything about you even if u dont know we even exist.</p>
                <p className="mb-2">
                    You are {user.sex}, your email is {user.email} and you were born
                    {user.birthday.getMonth()}.
                </p>
                <p className="mb-2">Your desired description is {user.subscriptionTier}.</p>
            </div>

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
                        <input
                            type="text"
                            name="name"
                            className="block appearance-none w-full py-1 px-2 mb-1 text-base leading-normal bg-white text-gray-800 border border-gray-200 rounded"
                            placeholder="John Doe"
                            value={formik.values.name}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                        />
                        {formik.errors.name && <div className="text-red-600">{formik.errors.name}</div>}
                    </label>
                </div>

                <div className="mb-3">
                    <label htmlFor="email" className="form-label">
                        Email
                        <input
                            type="email"
                            name="email"
                            className="block appearance-none w-full py-1 px-2 mb-1 text-base leading-normal bg-white text-gray-800 border border-gray-200 rounded"
                            placeholder="john@example.com"
                            value={formik.values.email}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                        />
                        {formik.errors.email && <div className="text-red-600">{formik.errors.email}</div>}
                    </label>
                </div>

                <div className="mb-3">
                    <label htmlFor="message" className="form-label">
                        Message
                        <textarea
                            name="message"
                            className="block appearance-none w-full py-1 px-2 mb-1 text-base leading-normal bg-white text-gray-800 border border-gray-200 rounded"
                            placeholder="Your message ..."
                            value={formik.values.message}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                        />
                        {formik.errors.message && <div className="text-red-600">{formik.errors.message}</div>}
                    </label>
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
