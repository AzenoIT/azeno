import { Meta, StoryObj } from "@storybook/react";
import AvatarComponent from "@azeno/bank/components/Avatar/Avatar";
import { ComponentProps } from "react";

export default {
    component: AvatarComponent,
    args: {
        src: "https://picsum.photos/id/237/140/140",
    },
} satisfies Meta<typeof AvatarComponent>;

type Props = ComponentProps<typeof AvatarComponent>;
export const Avatar: StoryObj<typeof AvatarComponent> = {
    render: ({ src, alt, type }: Props) => <AvatarComponent src={src} alt={alt} type={type} />,
};
