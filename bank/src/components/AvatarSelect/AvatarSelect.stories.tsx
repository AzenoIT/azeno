import { Meta, StoryObj } from "@storybook/react";

import AvatarSelectComponent from "@azeno/bank/components/AvatarSelect/AvatarSelect";
import { ComponentProps } from "react";

const meta = {
    component: AvatarSelectComponent,
} satisfies Meta<typeof AvatarSelectComponent>;

export default meta;

type Story = StoryObj<typeof AvatarSelectComponent>;
type Props = ComponentProps<typeof AvatarSelectComponent>;

export const AvatarSelect: Story = {
    render: ({}: Props) => <AvatarSelectComponent />,
};
