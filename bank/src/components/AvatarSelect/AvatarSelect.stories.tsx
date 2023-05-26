import { Meta, StoryObj } from "@storybook/react";

import AvatarSelectComponent from "@azeno/bank/components/AvatarSelect/AvatarSelect";

const meta = {
    component: AvatarSelectComponent,
} satisfies Meta<typeof AvatarSelectComponent>;

export default meta;

type Story = StoryObj<typeof AvatarSelectComponent>;

export const AvatarSelect: Story = {
    render: () => <AvatarSelectComponent />,
};
