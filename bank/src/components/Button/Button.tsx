import React from "react";

interface ButtonProps {
    onClick: (event: React.MouseEvent<HTMLButtonElement>) => void;
    children: React.ReactNode;
    color?: "primary" | "secondary" | "success" | "warning" | "error";
    size?: "sm" | "md" | "lg";
}

const colorConfig = {
    primary: "bg-primary text-white",
    secondary: "bg-secondary text-blue-900",
    success: "bg-success text-white",
    warning: "bg-warning text-white",
    error: "bg-error text-white",
};

const sizeConfig = {
    sm: "px-1 py-2 min-w-40",
    md: "py-2 px-4 min-w-60",
    lg: "py-3 px-6 min-w-80",
};

/**
 * This is an example of dummy button component
 */
export default function Button({ onClick, children, color = "primary", size = "md" }: ButtonProps) {
    const colorClasses = colorConfig[color];
    const sizeClasses = sizeConfig[size];

    return (
        <button type="button" className={`${colorClasses} ${sizeClasses}`} onClick={onClick}>
            {children}
        </button>
    );
}