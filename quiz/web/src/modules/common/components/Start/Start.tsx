import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Container from "@mui/material/Container";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import NavBar from "modules/common/components/Start/NavBar";
import CachedIcon from "@mui/icons-material/Cached";
import IconButton from "@mui/material/IconButton";
import InputAdornment from "@mui/material/InputAdornment";

function Start() {
    return (
        <div className="w-screen h-screen">
            <NavBar />
            <Container
                maxWidth="xl"
                sx={{ display: "flex", flexDirection: "column", alignItems: "center", my: 5, alignContent: "center" }}
            >
                <Typography className="m-2" variant="h2" gutterBottom>
                    Witaj!
                </Typography>
                <Typography variant="subtitle1" gutterBottom>
                    Wpisz swoją nazwę i zacznij grać.
                </Typography>
                <Box
                    component="form"
                    sx={{
                        "& .MuiTextField-root": { m: 1, width: "25ch" },
                    }}
                    noValidate
                    autoComplete="off"
                >
                    <TextField
                        id="standard-helperText"
                        label="losowa nazwa"
                        type="search"
                        helperText="Nazwę - zawsze możesz zmienić"
                        variant="filled"
                        size="small"
                        InputProps={{
                            endAdornment: (
                                <InputAdornment position="end">
                                    <IconButton type="button" sx={{ p: "5px", color: "#92A7FD" }} aria-label="search">
                                        <CachedIcon fontSize="large" />
                                    </IconButton>
                                </InputAdornment>
                            ),
                        }}
                        sx={{
                            "& .MuiInputBase-root": { bgcolor: "#DDE1FF" },
                        }}
                    />
                </Box>
                <Button variant="contained" sx={{ bgcolor: "#4459A9", borderRadius: 5, mt: 3.2 }}>
                    Zacznij grać
                </Button>

                <Button variant="contained" sx={{ bgcolor: "#DDE1FF", borderRadius: 5, mt: 8.3, color: "black" }}>
                    Logowanie
                </Button>
                <Button variant="contained" sx={{ bgcolor: "#DDE1FF", borderRadius: 5, mt: 4.5, color: "black" }}>
                    Rejestracja
                </Button>
            </Container>
        </div>
    );
}

export default Start;
