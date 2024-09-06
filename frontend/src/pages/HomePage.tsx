import { Flex, Image } from "@chakra-ui/react";
import SearchBar from "../components/SearchBar/SearchBar";
import logo from "../assets/whgg-logo.png";
import { SearchParams, useSearch } from "../hooks/useSearch";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

export function HomePage() {
  const { handleSearch, error, isLoading, result } = useSearch();
  const navigate = useNavigate();

  useEffect(() => {
    if (result) {
      navigate("/dashboard");
    }
  });
  const onSearch = (searchParams: SearchParams) => {
    handleSearch(searchParams);
  };

  return (
    <Flex
      height="70vh"
      direction={"column"}
      align="center"
      justifyContent="center"
    >
      <Image src={logo} alt="Logo" mb={8} width="300px" />
      <SearchBar
        handleSearch={onSearch}
        isLoading={isLoading}
        width="50%"
        height="10%"
      />
    </Flex>
  );
}
