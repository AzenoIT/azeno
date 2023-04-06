import type { Meta, StoryObj } from "@storybook/react";
import "index.css";

import Button from "components/Button";

const meta: Meta<typeof Button> = {
    title: "Button",
    component: Button,
    args: {
        color: "primary",
        size: "sm",
        children: "Button",
    },
};

export default meta;
type Story = StoryObj<typeof Button>;
export const Primary: Story = {
    render: ({ size, onClick, children, color }) => (
        <Button size={size} color={color} onClick={onClick}>
            {children}
        </Button>
    ),
};
