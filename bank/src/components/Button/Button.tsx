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
    sm: "py-1 px-2 min-w-[100px]",
    md: "py-2 px-4 min-w-[125px]",
    lg: "py-4 px-8 min-w-[150px]",
};

/**
 * This is a mockup of Button component with simple test example.
 */
export default function Button({ onClick, children, color = "primary", size = "md" }: ButtonProps) {
    const colorClasses = colorConfig[color];
    const sizeClasses = sizeConfig[size];

    return (
        <button type="button" className={`hover:opacity-90 ${colorClasses} ${sizeClasses}`} onClick={onClick}>
            {children}
        </button>
    );
}
