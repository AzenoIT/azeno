import { Avatar as AvatarMUI } from "@mui/material";

interface AvatarProps {
    src?: string;
    alt?: string;
    width?: number;
    height?: number;
}

export default function Avatar({ src, alt = "Avatar Picture", width = 140, height = 140 }: AvatarProps) {
    return <AvatarMUI src={src} alt={alt} sx={{ width, height }} className="border-[10px] border-tertiary-800" />;
}
