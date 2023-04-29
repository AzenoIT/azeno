import { Avatar as AvatarMUI } from "@mui/material";

type AvatarTypes = "sm" | "md" | "lg";

const typeConfig: { [key in AvatarTypes]: string } = {
    sm: "w-[50px] h-[50px] border-3 border-tertiary-800",
    md: "w-[70px] h-[70px] border-5 border-tertiary-800",
    lg: "w-[140px] h-[140px] border-10 border-tertiary-800",
};

interface AvatarProps {
    src?: string;
    alt?: string;
    type?: AvatarTypes;
}

export default function Avatar({ src, alt = "Avatar Picture", type = "md" }: AvatarProps) {
    const config = typeConfig[type];
    return <AvatarMUI src={src} alt={alt} className={config} />;
}
