import { Box, Center, Flex, Text, Square } from "@chakra-ui/react";
import LeagueEntryCard from "./LeagueEntries/LeagueEntryCard";
import ChampionStatsRow from "./ChampionStats/ChampionStatsRow";
import ChallengerEmblem from "../assets/Rank=Challenger.png";
import { MatchCard } from "./Matches/MatchCard";
import fiddleTile from "../assets/tiles/Fiddlesticks.png";
import { CardTitle } from "./ui/CardTitle";

function DashboardContent() {
  return (
    <Flex
      direction={"row"}
      position={"relative"}
      height={"auto"}
      _before={"absolute "}
    >
      {/* Left column */}
      <Flex
        pr={3}
        width="400px"
        bgColor={"background"}
        direction={"column"}
        height={"auto"}
      >
        <LeagueEntryCard
          title="Ranked Solo"
          emblemUrl={ChallengerEmblem}
          rank="Bronze 4"
          leaguePoints={0}
          wins={32}
          losses={12}
          wr={60}
        />

        <LeagueEntryCard
          title="Ranked Flex"
          emblemUrl={ChallengerEmblem}
          rank="Iron 3"
          leaguePoints={99}
          wins={52}
          losses={22}
          wr={40}
        />
        <Flex
          height={"59px"}
          bgColor={"secondary"}
          mb={"1px"}
          borderTopRightRadius={"3px"}
          borderTopLeftRadius={"3px"}
          align={"center"}
          pl={1}
        >
          <CardTitle text="Champion Stats" mt={1} ml={3} />
        </Flex>
        <ChampionStatsRow img={fiddleTile} />
        <ChampionStatsRow img={fiddleTile} />
        <ChampionStatsRow img={fiddleTile} />
        <ChampionStatsRow img={fiddleTile} />
        <ChampionStatsRow img={fiddleTile} />
        <ChampionStatsRow img={fiddleTile} />
        <ChampionStatsRow img={fiddleTile} />
      </Flex>
      {/* Right Column */}
      <Flex
        bgColor="#11112A"
        p={2}
        width="70%"
        direction={"column"}
        borderRadius={"3px"}
      >
        {/* Header */}
        <CardTitle text="Match History" mb={4} />
        <MatchCard bgColor="win" />
        <MatchCard bgColor="lose" />
        <MatchCard bgColor="win" />
        <MatchCard bgColor="lose" />
        <MatchCard bgColor="win" />
        <MatchCard bgColor="lose" />
        <MatchCard bgColor="win" />
      </Flex>
    </Flex>
  );
}

export default DashboardContent;
