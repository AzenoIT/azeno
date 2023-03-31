import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Container from "@mui/material/Container";
import Logo from "assets/logo.png";
import Typography from "@mui/material/Typography";

function NavBar() {
    return (
        <AppBar position="sticky" sx={{ bgcolor: "#4459A9" }}>
            <Container maxWidth="xl">
                <Toolbar disableGutters>
                    <img className="w-20 h-20" src={Logo} alt="logo" />
                    <Typography variant="h6" gutterBottom>
                        Azeno/Quiz
                    </Typography>
                </Toolbar>
            </Container>
        </AppBar>
    );
}

export default NavBar;
