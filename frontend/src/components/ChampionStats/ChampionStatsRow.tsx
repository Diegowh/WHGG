import { Flex, Text, Spacer } from "@chakra-ui/react";
import { ImageTile } from "../ui/ImageTile";

interface ChampionStatsRowProps {
  img: string;
  kda: number;
  winrate: number;
}
function ChampionStatsRow({ img, kda, winrate }: ChampionStatsRowProps) {
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
        maxWidth="70px"
      >
        {"Fiddlesticks"}
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
              ? "lightBlueText"
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
          color={"ligthBlueText"}
        >
          {"6.4"} / {"3.3"} / {"9.9"}
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
              ? "lightBlueText"
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
          color={"ligthBlueText"}
        >
          {"23"} games
        </Text>
      </Flex>
    </Flex>
  );
}

export default ChampionStatsRow;
