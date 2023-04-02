import Typography from "@mui/material/Typography";
import InputAdornment from "@mui/material/InputAdornment";
import IconButton from "@mui/material/IconButton";
import CachedIcon from "@mui/icons-material/Cached";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import NavBar from "./NavBar";

function Start() {
    return (
        <div className="container h-screen">
            <NavBar />
            <div className="flex flex-col items-center content-center my-5 mt-9">
                <Typography className="m-2" variant="h2" gutterBottom>
                    Witaj!
                </Typography>
                <Typography variant="subtitle1" gutterBottom>
                    Wpisz swoją nazwę i zacznij grać.
                </Typography>
                <TextField
                    id="standard-helperText"
                    placeholder="losowa nazwa"
                    helperText="Nazwę - zawsze możesz zmienić"
                    variant="filled"
                    size="small"
                    InputProps={{
                        endAdornment: (
                            <InputAdornment position="end">
                                <IconButton type="button" aria-label="search">
                                    <CachedIcon className="text-primary70" fontSize="large" />
                                </IconButton>
                            </InputAdornment>
                        ),
                    }}
                    sx={{
                        "& .MuiInputBase-root": { bgcolor: "#DDE1FF" },
                        "& .MuiFormHelperText-root ": { textAlign: "center" },
                    }}
                />
                <Button variant="contained" className="bg-primary40 rounded-full mt-6">
                    Zacznij grać
                </Button>
                <Button variant="contained" className="bg-secondary90 rounded-full mt-16 text-black">
                    Logowanie
                </Button>
                <Button variant="contained" className="bg-secondary90 rounded-full mt-9 text-black">
                    Rejestracja
                </Button>
            </div>
        </div>
    );
}

export default Start;
