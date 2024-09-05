import { Flex, Text, Spacer } from "@chakra-ui/react";
import { ImageTile } from "../ui/ImageTile";

interface ChampionStatsRowProps {
  img: string;
  kda: number;
  winrate: number;
  name: string;
  gamesPlayed: number;
  kills: number;
  deaths: number;
  assists: number;
}
function ChampionStatsRow({
  img,
  kda,
  winrate,
  name,
  gamesPlayed,
  kills,
  deaths,
  assists,
}: ChampionStatsRowProps) {
  return (
    <Flex
      bgColor={"secondary"}
      height={"59px"}
      direction={"row"}
      padding={3}
      marginBottom={"1px"}
    >
      <ImageTile img={img} />

      <Text
        fontSize="12px"
        fontWeight={600}
        alignSelf={"center"}
        marginLeft={"10px"}
        isTruncated
        maxWidth="55px"
      >
        {name}
      </Text>
      <Spacer />

      {/* KDA */}
      <Flex direction={"column"}>
        <Text
          fontSize="14px"
          alignSelf={"center"}
          fontWeight={600}
          color={
            kda < 1
              ? "redText"
              : kda < 3
              ? "lightblueText"
              : kda < 5
              ? "terciary"
              : "#FF9B00"
          }
        >
          {kda} KDA
        </Text>
        <Text
          fontSize="12px"
          fontWeight={600}
          alignSelf={"center"}
          color={"lightblueText"}
        >
          {kills} / {deaths} / {assists}
        </Text>
      </Flex>
      {/* WinRate */}
      <Spacer />
      <Flex direction={"column"}>
        <Text
          fontSize="12px"
          fontWeight={600}
          alignSelf={"end"}
          color={
            winrate < 60
              ? "lightblueText"
              : winrate < 75
              ? "terciary"
              : "orangeText"
          }
        >
          {winrate}%
        </Text>
        <Text
          fontSize="12px"
          fontWeight={600}
          alignSelf={"end"}
          color={"lightblueText"}
        >
          {gamesPlayed} games
        </Text>
      </Flex>
    </Flex>
  );
}

export default ChampionStatsRow;
