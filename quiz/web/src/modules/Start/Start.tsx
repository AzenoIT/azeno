import { useState, useEffect } from "react";
import Typography from "@mui/material/Typography";
import InputAdornment from "@mui/material/InputAdornment";
import IconButton from "@mui/material/IconButton";
import CachedIcon from "@mui/icons-material/Cached";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import { faker } from "@faker-js/faker";
import { Link } from "react-router-dom";
import NavBar from "./NavBar";

function Start() {
    const [userNickname, setUserNickname] = useState("");
    const [suggestedNickname, setSuggestedNickname] = useState("");

    function generateSuggestedNickname() {
        const generatedNickname = faker.internet.userName();
        setSuggestedNickname(generatedNickname);
    }

    useEffect(() => {
        generateSuggestedNickname();
    }, []);

    useEffect(() => {
        setUserNickname(suggestedNickname);
    }, [suggestedNickname]);
    return (
        <div className="container h-screen">
            <NavBar />
            <div className="flex flex-col items-center content-center m-5 mt-9">
                <Typography className="mb-3" variant="h4" gutterBottom>
                    Witaj!
                </Typography>
                <Typography variant="subtitle1" gutterBottom>
                    Wpisz swoją nazwę i zacznij grać.
                </Typography>
                <TextField
                    id="standard-helperText"
                    className="pt-10"
                    placeholder="losowa nazwa"
                    helperText="Nazwę zawsze możesz zmienić"
                    variant="filled"
                    size="small"
                    value={userNickname}
                    onChange={(event) => setUserNickname(event.target.value)}
                    InputProps={{
                        endAdornment: (
                            <InputAdornment position="end">
                                <IconButton
                                    type="button"
                                    aria-label="search"
                                    onClick={() => {
                                        generateSuggestedNickname();
                                        setUserNickname(suggestedNickname);
                                    }}
                                >
                                    <CachedIcon className="text-primary70" fontSize="large" />
                                </IconButton>
                            </InputAdornment>
                        ),
                    }}
                    sx={{
                        "& .MuiInputBase-root": { bgcolor: "#DDE1FF", textAlign: "center", padding: 0 },
                        "& .MuiInputBase-input": { padding: 1 },
                        "& .MuiFormHelperText-root ": { textAlign: "center" },
                    }}
                />
                <Typography align="center" variant="body1">
                    Dobre nazwy są krótkie i łatwe do zapamiętania! Potrzebujesz inspiracji? Co ty na{" "}
                    <span
                        style={{ color: "green", cursor: "pointer" }}
                        onClick={() => setUserNickname(suggestedNickname)}
                    >
                        {suggestedNickname}
                    </span>
                    ?
                </Typography>
                <Button
                    variant="contained"
                    className="bg-primary40 rounded-full mt-6"
                    disabled={!userNickname || userNickname.length <= 3}
                >
                    Zacznij grać
                </Button>
                <Button variant="contained" className="bg-secondary90 rounded-full mt-16 text-black">
                    <Link to="/login">Logowanie</Link>
                </Button>
                <Button variant="contained" className="bg-secondary90 rounded-full mt-9 text-black">
                    <Link to="/register">Rejestracja</Link>
                </Button>
            </div>
        </div>
    );
}

export default Start;
