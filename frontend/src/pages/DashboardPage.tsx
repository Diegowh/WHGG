import { Box, Flex } from "@chakra-ui/react";
import HeaderBar from "../components/HeaderBar";

import { ProfileCard } from "../components/Profile/ProfileCard";
import DashboardContent from "../components/DashboardContent";
import { useSearch } from "../hooks/useSearch";

export function DashboardPage() {
  const { handleSearch, error, isLoading, result } = useSearch();

  return (
    <Flex direction="column" height="auto" bgColor={"backgound"}>
      <HeaderBar handleSearch={handleSearch} isLoading={isLoading} />
      {/* Dashboard Content */}
      <Flex overflow="auto" flex="1" justifyContent="center">
        <Box borderRadius={5} width="1000px">
          <ProfileCard data={result} />
          <DashboardContent data={result} />
        </Box>
      </Flex>
    </Flex>
  );
}
