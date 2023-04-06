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
export const Buttons: Story = {
    render: ({ onClick }) => (
        <div className="flex flex-col justify-evenly h-96">
            <div className="flex justify-evenly">
                <Button size="sm" color="primary" onClick={onClick}>
                    Primary
                </Button>
                <Button size="sm" color="secondary" onClick={onClick}>
                    Secondary
                </Button>
                <Button size="sm" color="success" onClick={onClick}>
                    Success
                </Button>
                <Button size="sm" color="warning" onClick={onClick}>
                    Warning
                </Button>
                <Button size="sm" color="error" onClick={onClick}>
                    Error
                </Button>
            </div>
            <div className="flex justify-evenly">
                <Button size="md" color="primary" onClick={onClick}>
                    Primary
                </Button>
                <Button size="md" color="secondary" onClick={onClick}>
                    Secondary
                </Button>
                <Button size="md" color="success" onClick={onClick}>
                    Success
                </Button>
                <Button size="md" color="warning" onClick={onClick}>
                    Warning
                </Button>
                <Button size="md" color="error" onClick={onClick}>
                    Error
                </Button>
            </div>
            <div className="flex justify-evenly">
                <Button size="lg" color="primary" onClick={onClick}>
                    Primary
                </Button>
                <Button size="lg" color="secondary" onClick={onClick}>
                    Secondary
                </Button>
                <Button size="lg" color="success" onClick={onClick}>
                    Success
                </Button>
                <Button size="lg" color="warning" onClick={onClick}>
                    Warning
                </Button>
                <Button size="lg" color="error" onClick={onClick}>
                    Error
                </Button>
            </div>
        </div>
    ),
};
