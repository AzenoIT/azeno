import type { Meta, StoryObj } from "@storybook/react";
import { within, userEvent } from "@storybook/testing-library";

import { expect } from "@storybook/jest";

import "index.css";

import Button from "components/Button";

const meta: Meta<typeof Button> = {
    title: "Button",
    component: Button,
    tags: ["autodocs"],
};

export default meta;
type Story = StoryObj<typeof Button>;
export const AllVariants: Story = {
    render: ({ onClick }) => {
        const rows = ["primary", "secondary", "success", "warning", "error"].flatMap(
            (color: "primary" | "secondary" | "success" | "warning" | "error") =>
                ["sm", "md", "lg"].map((size: "sm" | "md" | "lg") => (
                    <div key={size + color} className="flex items-center justify-center">
                        <Button size={size} color={color} onClick={onClick}>
                            {`${color} ${size}`}
                        </Button>
                    </div>
                ))
        );
        return <div className="grid grid-cols-3 gap-x-10 gap-y-5">{rows}</div>;
    },
    argTypes: {
        size: { control: false },
        color: { control: false },
        onClick: { control: false },
        children: { control: false },
    },
};

export const PlayGround: Story = {
    render: ({ onClick, color, size, children }) => (
        <div className="flex items-center justify-center min-h-[300px]">
            <Button onClick={onClick} color={color} size={size}>
                {children}
            </Button>
        </div>
    ),
    play: async ({ canvasElement }) => {
        const canvas = within(canvasElement);

        const button: HTMLButtonElement = canvas.getByRole("button");
        await userEvent.hover(button);

        expect(button.textContent).toBe("Button");
    },
    args: {
        size: "md",
        color: "primary",
        children: "Button",
    },
};
