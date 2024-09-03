import { Flex, Image } from "@chakra-ui/react";
import SearchBar from "../components/SearchBar/SearchBar";
import logo from "../assets/whgg-logo.png";

export function HomePage() {
  return (
    <Flex
      height="70vh"
      direction={"column"}
      align="center"
      justifyContent="center"
    >
      <Image src={logo} alt="Logo" mb={8} width="300px" />
      <SearchBar width="50%" height="10%" />
    </Flex>
  );
}
