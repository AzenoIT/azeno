import { useState } from "react";
import ImagePicker from "./ImagePicker";

function AddDeck() {
    const [selectedImage, setSelectedImage] = useState<string | null>(null);

    return (
        <div
            style={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                minHeight: "100vh",
                background: "radial-gradient(circle at center, #2D4E9D 50%, #273569)",
            }}
        >
            <h1 style={{ fontSize: "2rem", color: "white" }}>Dodaj nowy deck</h1>
            <div
                style={{
                    maxWidth: "600px",
                    width: "100%",
                    backgroundColor: "#2c3e5080",
                    borderRadius: "15px",
                    marginTop: "1rem",
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    overflow: "hidden",
                }}
            >
                <div
                    style={{
                        backgroundImage: selectedImage ? `url(${selectedImage})` : "none",
                        backgroundPosition: "center",
                        backgroundRepeat: "no-repeat",
                        backgroundSize: "cover",
                        position: "relative",
                        maxWidth: "100%",
                        width: "100%",
                        height: "164px",
                    }}
                />
                <form
                    style={{
                        display: "flex",
                        flexDirection: "column",
                        alignItems: "center",
                        marginTop: "1rem",
                        marginBottom: "1rem",
                        width: "100%",
                        padding: "0 1rem",
                    }}
                >
                    <label htmlFor="deckName" style={{ fontSize: "1.25rem", color: "white" }}>
                        Nazwa decka:
                    </label>
                    <input
                        type="text"
                        id="deckName"
                        name="deckName"
                        style={{
                            fontSize: "1.25rem",
                            padding: "0.5rem",
                            borderRadius: "5px",
                            width: "100%",
                            marginBottom: "1rem",
                        }}
                    />
                    <label htmlFor="category" style={{ fontSize: "1.25rem", color: "white" }}>
                        Kategoria:
                    </label>
                    <select
                        id="category"
                        name="category"
                        style={{
                            fontSize: "1.25rem",
                            padding: "0.5rem",
                            borderRadius: "5px",
                            width: "100%",
                        }}
                    >
                        <option value="javascript">JavaScript</option>
                        <option value="python">Python</option>
                        <option value="react">React</option>
                        <option value="node">Node.js</option>
                        <option value="ruby">Ruby</option>
                    </select>
                </form>
            </div>
            <ImagePicker setSelectedImage={setSelectedImage} />
        </div>
    );
}

export default AddDeck;
