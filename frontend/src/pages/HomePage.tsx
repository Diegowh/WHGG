import { Flex, Image } from "@chakra-ui/react";
import SearchBar from "../components/SearchBar/SearchBar";
import logo from "../assets/whgg-logo.png";
import { useSearch } from "../hooks/useSearch";
import { useNavigate } from "react-router-dom";

export function HomePage() {
  const { handleSearch, error, isLoading, result } = useSearch();

  return (
    <Flex
      height="70vh"
      direction={"column"}
      align="center"
      justifyContent="center"
    >
      <Image src={logo} alt="Logo" mb={8} width="300px" />
      <SearchBar
        handleSearch={handleSearch}
        isLoading={isLoading}
        width="50%"
        height="10%"
      />
    </Flex>
  );
}
