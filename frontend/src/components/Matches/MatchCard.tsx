import { Flex, Text, Image, Box } from "@chakra-ui/react";
import { ImageTile } from "../ui/ImageTile";
import { ParticipantRow } from "./ParticipantRow";
import testTile from "../../assets/tiles/Jhin.png";
import item0 from "../../assets/img/item/6657.png";
import item1 from "../../assets/img/item/3020.png";
import item2 from "../../assets/img/item/3137.png";
import item3 from "../../assets/img/item/3089.png";

import item6 from "../../assets/img/item/2052.png";
import { Match } from "../../interfaces";
import queues from "../../utils/queues.json";
import summonerSpells from "../../utils/summonerSpells.json";
import { getChampionTileUrl } from "../../utils/utils";

const runeWinColor: string = "#223B80";
const runeLoseColor: string = "#53263E";

type MatchCardProps = {
  match: Match;
};
export function MatchCard({ match }: MatchCardProps) {
  console.log("EEEEEEEEEEEEEEEEEEEE");
  console.log(JSON.stringify(match, null, 2));
  const runeBgColor = match.win ? runeWinColor : runeLoseColor;
  const cardBgColor = match.win ? "win" : "lose";
  const renderItem = (itemSrc: string | undefined) => (
    <Box
      boxSize={"25px"}
      borderRadius={4}
      bgColor={itemSrc ? "transparent" : runeBgColor}
      margin={"0.5px"}
      // padding={"1px"}
    >
      {itemSrc && (
        <Image
          src={itemSrc}
          boxSize={"100%"}
          borderRadius={4}
          objectFit="cover"
          padding={"1px"}
        />
      )}
    </Box>
  );
  const getSpellImageUrl = (spellId: number): string | undefined => {
    const spell = summonerSpells.find((spell) => spell.id === spellId);
    if (spell) {
      try {
        return new URL(`../../assets/img/spell/${spell.image}`, import.meta.url)
          .href;
      } catch (error) {
        return undefined;
      }
    } else {
      console.log("NO ENCONTRO EL SPELL ID");
    }
  };

  const getQueueName = (queueId: number) => {
    const queue = queues.find((q) => q.queueId === queueId);
    return queue ? queue.name : "Unknown Mode";
  };

  const getKda = (k: number, d: number, a: number) => {
    if (d === 0) {
      return parseFloat((k + a).toFixed(2));
    }
    return parseFloat(((k + a) / d).toFixed(2));
  };

  const getCsPerMin = (cs: number, totalTime: number) => {
    const totalMinutes = totalTime / 60;
    return parseFloat((cs / totalMinutes).toFixed(1));
  };
  const formatTime = (seconds: number): string => {
    const minutes = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${minutes}:${secs.toString().padStart(2, "0")}`;
  };
  const kda = getKda(match.kills, match.deaths, match.assists);
  const summonerSpell1 = getSpellImageUrl(match.summoner1Id);
  const summonerSpell2 = getSpellImageUrl(4);

  const getPerkUrl = (perkId: number) => {
    try {
      return new URL(`../../assets/img/runes/${perkId}.png`, import.meta.url)
        .href;
    } catch (error) {
      return undefined;
    }
  };
  return (
    <Flex
      bgColor={cardBgColor}
      direction={"row"}
      marginInline={3}
      marginTop={1}
      h={"100px"}
      borderRadius={3}
      alignItems={"center"}
    >
      {/* Columna 0 */}
      <Flex
        direction={"column"}
        alignItems={"center"}
        // justifyContent={"center"}
        margin={4}
      >
        <Text fontSize="11px" fontWeight={600}>
          {getQueueName(match.queueId)}
        </Text>
        <Text fontSize="11px" fontWeight={400} color={"lightblueText"} pb={3}>
          4 days ago
        </Text>
        <Flex direction={"row"}>
          <Text
            fontSize="11px"
            fontWeight={600}
            pr={1}
            color={match.win ? "terciary" : "redText"}
          >
            WIN
          </Text>
          <Text fontSize="11px" fontWeight={600} color="lightblueText">
            {formatTime(match.gameDuration)}
          </Text>
        </Flex>
      </Flex>
      {/* Columna 1 / Imagen */}

      <ImageTile img={getChampionTileUrl(match.championName)} boxSize="50px" />
      {/* Columna 2 y 3 / SummSpells y Runas */}
      <Flex direction={"column"}>
        {renderItem(summonerSpell1)}
        {renderItem(summonerSpell2)}
      </Flex>
      <Flex direction={"column"} marginRight={4}>
        <Box
          boxSize={"25px"}
          borderRadius={4}
          bgColor={runeBgColor}
          margin={"0.5px"}
          // padding={"1px"}
        >
          <Image
            src={getPerkUrl(match.perk0)}
            boxSize={"100%"}
            borderRadius={4}
            objectFit="cover"
            padding={"1px"}
          />
        </Box>
        <Box
          boxSize={"25px"}
          borderRadius={4}
          bgColor={runeBgColor}
          margin={"0.5px"}
        >
          <Image
            src={getPerkUrl(match.perk1)}
            boxSize={"100%"}
            borderRadius={4}
            objectFit="cover"
            padding={"1px"}
          />
        </Box>
      </Flex>
      {/* Columna 4 / Score y KDA */}
      <Flex direction={"column"} alignItems={"center"} mr={4}>
        {/* Línea de Kills / Deaths / Assists */}
        <Text fontSize="15px" fontWeight={600}>
          <Text as="span" color="white">
            {match.kills}
          </Text>{" "}
          /{" "}
          <Text as="span" color="#FF4E50">
            {match.deaths}
          </Text>{" "}
          /{" "}
          <Text as="span" color="white">
            {match.assists}
          </Text>
        </Text>
        {/* Línea de KDA */}
        <Text fontSize="10px" fontWeight={300}>
          <Text
            as="span"
            color={
              kda < 1
                ? "redText"
                : kda < 3
                ? "white"
                : kda < 5
                ? "terciary"
                : "#FF9B00"
            }
            fontWeight={800}
          >
            {kda}
          </Text>{" "}
          <Text as="span" color="lightblueText">
            KDA
          </Text>
        </Text>
        <Text fontSize="10px" fontWeight={300} color="lightblueText">
          {match.totalMinionsKilled} CS (
          {getCsPerMin(match.totalMinionsKilled, match.gameDuration)})
        </Text>
      </Flex>
      {/* Columnas de Items */}
      <Flex direction={"column"}>
        {renderItem(item0)}
        {renderItem(item3)}
      </Flex>
      <Flex direction={"column"}>
        {renderItem(item1)}
        {renderItem(undefined)}
      </Flex>
      <Flex direction={"column"}>
        {renderItem(item2)}
        {renderItem(undefined)}
      </Flex>
      <Flex direction={"column"} mr={4}>
        {renderItem(item6)}
        <Box
          boxSize={"25px"}
          borderRadius={4}
          bgColor={"transparent"}
          margin={"0.5px"}
          // padding={"1px"}
        ></Box>
      </Flex>
      {/* Columna Equipo 1 */}
      <Flex direction={"column"} mr={4}>
        <ParticipantRow img={testTile} riotId="Flatulent paco" />
        <ParticipantRow img={testTile} riotId="w00tfighter" />
        <ParticipantRow img={testTile} riotId="oaisjdoadjkals" />
        <ParticipantRow img={testTile} riotId="oaisjdoadjkals" />
        <ParticipantRow img={testTile} riotId="oaisjdoadjkals" />
      </Flex>
      {/* Columna Equipo 2 */}
      <Flex direction={"column"}>
        <ParticipantRow img={testTile} riotId="oaisjdoadjkals" />
        <ParticipantRow img={testTile} riotId="oaisjdoadjkals" />
        <ParticipantRow img={testTile} riotId="oaisjdoadjkals" />
        <ParticipantRow img={testTile} riotId="oaisjdoadjkals" />
        <ParticipantRow img={testTile} riotId="oaisjdoadjkals" />
      </Flex>
    </Flex>
  );
}
