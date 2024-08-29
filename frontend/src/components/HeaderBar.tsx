import SearchBar from "./SearchBar/SearchBar";
import { Box, Image } from "@chakra-ui/react";
import logo from "../assets/whgg-logo.png";

function HeaderBar() {
  return (
    <Box
      height="8vh"
      display="flex"
      flexDirection="row"
      // alignItems="center"
      justifyContent="center"
      // backgroundColor={"red"}
      pr={"30px"}
      pt={"20px"}
    >
      <Image src={logo} alt="Logo" mt={1} height="30px" marginRight="5" />
      <SearchBar />
    </Box>
  );
}
export default HeaderBar;
