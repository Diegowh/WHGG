import { Box, Flex } from "@chakra-ui/react";
import HeaderBar from "../components/HeaderBar";

import { ProfileCard } from "../components/Profile/ProfileCard";
import DashboardContent from "../components/DashboardContent";
import { useSearch } from "../hooks/useSearch";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

export function DashboardPage() {
  const { handleSearch, isLoading: searchLoading, result } = useSearch();
  const [updateLoading, setUpdateLoading] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    if (result) {
      localStorage.setItem("searchResult", JSON.stringify(result));
    }
  }, [result]);

  useEffect(() => {
    const savedResult = localStorage.getItem("searchResult");
    const finalResult =
      result || (savedResult ? JSON.parse(savedResult) : null);

    if (!finalResult) {
      navigate("/");
    }
  }, [result, navigate]);

  const handleUpdate = async () => {
    setUpdateLoading(true);
    const savedResult = localStorage.getItem("searchResult");
    if (savedResult) {
      const { gameName, tagLine, server } = JSON.parse(savedResult);
      await handleSearch({ gameName, tagLine, server });
    }
    setUpdateLoading(false);
  };
  const savedResult = localStorage.getItem("searchResult");
  const finalResult = result || (savedResult ? JSON.parse(savedResult) : null);

  return (
    <Flex direction="column" height="auto" bgColor="backgound">
      <HeaderBar handleSearch={handleSearch} isLoading={searchLoading} />
      {/* Dashboard Content */}
      <Flex overflow="auto" flex="1" justifyContent="center">
        <Box borderRadius={5} width="1000px">
          <ProfileCard
            data={finalResult}
            onUpdate={handleUpdate}
            isLoading={updateLoading}
          />
          <DashboardContent data={finalResult} />
        </Box>
      </Flex>
    </Flex>
  );
}
