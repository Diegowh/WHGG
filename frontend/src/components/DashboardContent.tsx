import { filter, Flex, Text } from "@chakra-ui/react";
import LeagueEntryCard from "./LeagueEntries/LeagueEntryCard";
import ChampionStatsRow from "./ChampionStats/ChampionStatsRow";
import { MatchCard } from "./Matches/MatchCard";
import { CardTitle } from "./ui/CardTitle";
import { SearchResponse } from "../interfaces";
import { getChampionTileUrl, getWinrate } from "../utils/utils";
import rankEmblems from "../utils/emblems";
import { capitalize } from "../utils/utils";

interface DashboardContentProps {
  data: SearchResponse | null;
}

const defaultEntry = {
  queueType: "Unranked",
  tier: "",
  rank: "Unranked",
  leaguePoints: 0,
  wins: 0,
  losses: 0,
  wr: 0,
};

const getEmblemUrl = (rank: string) =>
  rankEmblems[rank as keyof typeof rankEmblems] || rankEmblems["IRON"];

function DashboardContent({ data }: DashboardContentProps) {
  const {
    leagueEntries = [],
    championStats = [],
    matches = [],
  } = data || { leagueEntries: [], championStats: [], matches: [] };

  const soloEntry =
    leagueEntries.find((entry) => entry.queueType === "RANKED_SOLO_5x5") ||
    defaultEntry;
  const flexEntry =
    leagueEntries.find((entry) => entry.queueType === "RANKED_FLEX_SR") ||
    defaultEntry;

  const sortedChampionStats = championStats
    .sort((a, b) => b.gamesPlayed - a.gamesPlayed)
    .slice(0, 7);
  const filteredMatches = matches
    .filter((match) => ![1700, 1810, 1820, 1830, 1840].includes(match.queueId))
    .slice(0, 20);

  return (
    <Flex direction={"row"} position={"relative"} height={"auto"}>
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
          emblemUrl={getEmblemUrl(soloEntry.tier)}
          rank={capitalize(soloEntry.tier) + " " + soloEntry.rank}
          leaguePoints={soloEntry.leaguePoints}
          wins={soloEntry.wins}
          losses={soloEntry.losses}
          wr={getWinrate(soloEntry.wins, soloEntry.losses)}
        />

        <LeagueEntryCard
          title="Ranked Flex"
          emblemUrl={getEmblemUrl(flexEntry.tier)}
          rank={capitalize(flexEntry.tier) + " " + flexEntry.rank}
          leaguePoints={flexEntry.leaguePoints}
          wins={flexEntry.wins}
          losses={flexEntry.losses}
          wr={getWinrate(flexEntry.wins, flexEntry.losses)}
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
        {sortedChampionStats.length > 0 ? (
          sortedChampionStats.map((champion) => (
            <ChampionStatsRow
              key={champion.id}
              img={getChampionTileUrl(champion.name)}
              kda={champion.kda}
              winrate={champion.winrate}
              name={champion.name}
              gamesPlayed={champion.gamesPlayed}
              kills={champion.killAvg}
              deaths={champion.deathAvg}
              assists={champion.assistAvg}
            />
          ))
        ) : (
          <Text> No champion stats available</Text>
        )}
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
        {filteredMatches.length > 0 ? (
          filteredMatches.map((filteredMatch) => (
            <MatchCard key={filteredMatch.id} match={filteredMatch} />
          )) // Mapear los matches ya filtrados y limitados
        ) : (
          <Text>No matches available</Text>
        )}
      </Flex>
    </Flex>
  );
}

export default DashboardContent;
