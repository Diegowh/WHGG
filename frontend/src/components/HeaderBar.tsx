import SearchBar from "./SearchBar/SearchBar";
import { Box, Image } from "@chakra-ui/react";
import logo from "../assets/whgg-logo.png";

interface HeaderBarProps {
  handleSearch: (params: {
    gameName: string;
    tagLine: string;
    server: string;
  }) => void;
  isLoading: boolean;
}

function HeaderBar({ handleSearch, isLoading }: HeaderBarProps) {
  return (
    <Box
      height="75px"
      display="flex"
      flexDirection="row"
      top="0"
      zIndex="1000"
      position={"sticky"}
      justifyContent="center"
      backgroundColor={"background"}
      pr={"30px"}
      pt={"20px"}
    >
      <Image src={logo} alt="Logo" mt={1} height="30px" marginRight="5" />
      <SearchBar handleSearch={handleSearch} isLoading={isLoading} />
    </Box>
  );
}
export default HeaderBar;
