import Avatar from "@azeno/bank/components/Avatar";
import EditIcon from "@mui/icons-material/Edit";
import { Dialog } from "@mui/material";

import AvatarEditor from "react-avatar-editor";
import { ChangeEvent, useRef, useState } from "react";

function useAvatarImage() {
    const [image, setImage] = useState<string>("");
    const [tempImage, setTempImage] = useState<string>("");

    function addTempImage(event: ChangeEvent<HTMLInputElement>) {
        if (!event.target.files) return;
        setTempImage(URL.createObjectURL(event.target.files[0]));
    }

    function uploadImage(canvas: HTMLCanvasElement) {
        setImage(canvas.toDataURL());
        setTempImage("");
    }

    return { image, tempImage, addTempImage, uploadImage, cancel: () => setTempImage("") };
}

interface AvatarSelectProps {
    alt?: string;
}

export default function AvatarSelect({ alt = "Profile picture" }: AvatarSelectProps) {
    const { image, tempImage, addTempImage, uploadImage, cancel } = useAvatarImage();
    const editor = useRef<AvatarEditor>(null);

    const handleResizeCompleted = () => {
        if (!editor.current) return;
        uploadImage(editor.current.getImage());
    };

    return (
        <>
            <Dialog open={tempImage !== ""} onClose={cancel}>
                <div className="p-4 flex flex-col items-center">
                    <AvatarEditor
                        ref={editor}
                        image={tempImage}
                        width={250}
                        height={250}
                        border={50}
                        color={[255, 255, 255, 0.6]} // RGBA
                        scale={1}
                    />
                    <button
                        type="button"
                        onClick={handleResizeCompleted}
                        className="max-w-[200px] bg-primary-600 text-white"
                    >
                        Upload
                    </button>
                </div>
            </Dialog>
            <div className="flex items-center gap-x-2.5">
                <div className="w-6" />
                <Avatar src={image} alt={alt} type="lg" />
                <label htmlFor="avatarImagePicker" className="w-6 cursor-pointer">
                    <input
                        id="avatarImagePicker"
                        type="file"
                        alt={alt}
                        src={image}
                        accept="image/*"
                        onChange={addTempImage}
                        className="hidden"
                    />
                    <EditIcon style={{ fill: "#3BAEE1" }} />
                </label>
            </div>
        </>
    );
}
