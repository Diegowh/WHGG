import { Flex } from "@chakra-ui/react";
import LeagueEntryCard from "./LeagueEntries/LeagueEntryCard";
import ChampionStatsRow from "./ChampionStats/ChampionStatsRow";
import PlatinumEmblem from "../assets/emblems/Rank=Platinum.png";
import EmeraldEmblem from "../assets/emblems/Rank=Emerald.png";
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
          emblemUrl={EmeraldEmblem}
          rank="Emerald 2"
          leaguePoints={0}
          wins={32}
          losses={12}
          wr={60}
        />

        <LeagueEntryCard
          title="Ranked Flex"
          emblemUrl={PlatinumEmblem}
          rank="Platinum 1"
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
        <ChampionStatsRow img={fiddleTile} kda={3.47} winrate={75} />
        <ChampionStatsRow img={fiddleTile} kda={0.33} winrate={12} />
        <ChampionStatsRow img={fiddleTile} kda={1.65} winrate={12} />
        <ChampionStatsRow img={fiddleTile} kda={3.11} winrate={12} />
        <ChampionStatsRow img={fiddleTile} kda={6.27} winrate={12} />
        <ChampionStatsRow img={fiddleTile} kda={2.77} winrate={12} />
        <ChampionStatsRow img={fiddleTile} kda={1.39} winrate={12} />
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
        <MatchCard win="win" kda={9.75} />
      </Flex>
    </Flex>
  );
}

export default DashboardContent;
