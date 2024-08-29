import { Box, Image } from "@chakra-ui/react";
import SearchBar from "../components/SearchBar/SearchBar";
import logo from "../assets/wh-logo.png";

function Home() {
  return (
    <Box
      height="70vh"
      display="flex"
      flexDirection="column"
      alignItems="center"
      justifyContent="center"
    >
      <Image src={logo} alt="Logo" mb={8} />
      <SearchBar />
    </Box>
  );
}

export default Home;