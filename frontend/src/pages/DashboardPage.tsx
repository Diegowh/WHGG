import { Box, Flex } from "@chakra-ui/react";
import HeaderBar from "../components/HeaderBar";

import { ProfileCard } from "../components/Profile/ProfileCard";
import DashboardContent from "../components/DashboardContent";

export function DashboardPage() {
  return (
    <Flex direction="column" height="auto" bgColor={"backgound"}>
      <HeaderBar />
      {/* Dashboard Content */}
      <Flex overflow="auto" flex="1" justifyContent="center">
        <Box borderRadius={5} width="1000px">
          <ProfileCard />
          <DashboardContent />
        </Box>
      </Flex>
    </Flex>
  );
}
