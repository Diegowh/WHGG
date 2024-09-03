import { Flex, Box, Text } from "@chakra-ui/react";
import ChampionStatsRow from "./ChampionStatsRow";
import fiddleTile from "../../assets/tiles/Fiddlesticks.png";

function ChampionStatsCard() {
  return (
    <Flex
      p={2}
      height={"auto"}
      width="100%"
      bgColor={"secondary"}
      direction={"column"}
    >
      <Box height={"59px"} bgColor={"gray"}>
        <Text fontSize="s" fontWeight={600} pt={3} pl={5}>
          Champion Stats
        </Text>
      </Box>

      <ChampionStatsRow img={fiddleTile} />
      <ChampionStatsRow img={fiddleTile} />
      <ChampionStatsRow img={fiddleTile} />
      <ChampionStatsRow img={fiddleTile} />
      <ChampionStatsRow img={fiddleTile} />
      <ChampionStatsRow img={fiddleTile} />
      <ChampionStatsRow img={fiddleTile} />
    </Flex>
  );
}

export default ChampionStatsCard;
