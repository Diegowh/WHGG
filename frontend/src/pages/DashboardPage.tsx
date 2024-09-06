import { Box, Flex } from "@chakra-ui/react";
import HeaderBar from "../components/HeaderBar";

import { ProfileCard } from "../components/Profile/ProfileCard";
import DashboardContent from "../components/DashboardContent";
import { useSearch } from "../hooks/useSearch";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

export function DashboardPage() {
  const { handleSearch, error, isLoading, result } = useSearch();
  const navigate = useNavigate();

  const savedResult = localStorage.getItem("searchResult");
  const finalResult = result || (savedResult ? JSON.parse(savedResult) : null);

  useEffect(() => {
    if (result !== null) {
      localStorage.setItem("searchResult", JSON.stringify(result));
    }
  }, [result]);

  useEffect(() => {
    if (!finalResult) {
      navigate("/");
    }
  }, [result, navigate]);

  return (
    <Flex direction="column" height="auto" bgColor={"backgound"}>
      <HeaderBar handleSearch={handleSearch} isLoading={isLoading} />
      {/* Dashboard Content */}
      <Flex overflow="auto" flex="1" justifyContent="center">
        <Box borderRadius={5} width="1000px">
          <ProfileCard data={finalResult} />
          <DashboardContent data={finalResult} />
        </Box>
      </Flex>
    </Flex>
  );
}
