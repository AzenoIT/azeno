import Typography from "@mui/material/Typography";
import NavBar from "modules/common/components/Start/NavBar";

function Start() {
    return (
        <>
            <NavBar />
            <Typography variant="h1" gutterBottom>
                Witaj
            </Typography>
            <Typography variant="subtitle1" gutterBottom>
                Wpisz swoją nazwę i zacznij grać.
            </Typography>
        </>
    );
}

export default Start;
