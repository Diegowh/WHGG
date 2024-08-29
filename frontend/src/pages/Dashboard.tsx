import { Box } from "@chakra-ui/react";
import HeaderBar from "../components/HeaderBar";

import ProfileCard from "../components/Profile/ProfileCard";

function Dashboard() {
  return (
    <Box display="flex" flexDirection="column" height="100vh">
      <HeaderBar />
      <Box
        overflow="auto"
        flex="1"
        display="flex"
        justifyContent="center"
        mt="5px"
      >
        <Box
          //bgColor="purple"
          borderRadius={5}
          width="1000px"
        >
          <ProfileCard />
        </Box>
      </Box>
    </Box>
  );
}

export default Dashboard;
