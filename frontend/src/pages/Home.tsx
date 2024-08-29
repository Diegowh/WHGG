import { Box, Image } from "@chakra-ui/react";
import SearchBar from "../components/SearchBar/SearchBar";
import logo from "../assets/whgg-logo.png";

function Home() {
  return (
    <Box
      height="70vh"
      display="flex"
      flexDirection="column"
      alignItems="center"
      justifyContent="center"
    >
      <Image src={logo} alt="Logo" mb={8} width="300px" />
      <SearchBar width="50%" height="10%" />
    </Box>
  );
}

export default Home;
