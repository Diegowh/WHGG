import { Flex, Text, Image, Box } from "@chakra-ui/react";
import { ImageTile } from "../ui/ImageTile";
import { ParticipantRow } from "./ParticipantRow";
import testTile from "../../assets/tiles/Jhin.png";
import summSpell1 from "../../assets/img/spell/SummonerHaste.png";
import summSpell2 from "../../assets/img/spell/SummonerFlash.png";
import rune1 from "../../assets/img/DarkHarvest.png";
import rune2 from "../../assets/img/7201_Precision.png";
import item0 from "../../assets/img/item/6657.png";
import item1 from "../../assets/img/item/3020.png";
import item2 from "../../assets/img/item/3137.png";
import item3 from "../../assets/img/item/3089.png";

import item6 from "../../assets/img/item/2052.png";

const runeWinColor: string = "#223B80";
const runeLoseColor: string = "#53263E";

type MatchCardProps = {
  win: string;
  kda: number;
};
export function MatchCard({ win, kda }: MatchCardProps) {
  const runeBgColor = win === "win" ? runeWinColor : runeLoseColor;
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
  return (
    <Flex
      bgColor={win}
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
          ARAM
        </Text>
        <Text fontSize="11px" fontWeight={400} color={"ligthBlueText"} pb={3}>
          4 days ago
        </Text>
        <Flex direction={"row"}>
          <Text
            fontSize="11px"
            fontWeight={600}
            pr={1}
            color={win === "win" ? "terciary" : "redText"}
          >
            WIN
          </Text>
          <Text fontSize="11px" fontWeight={600}>
            19:11
          </Text>
        </Flex>
      </Flex>
      {/* Columna 1 / Imagen */}

      <ImageTile img={testTile} boxSize="50px" />
      {/* Columna 2 y 3 / SummSpells y Runas */}
      <Flex direction={"column"}>
        {renderItem(summSpell1)}
        {renderItem(summSpell2)}
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
            src={rune1}
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
          // padding={"1px"}
        >
          <Image
            src={rune2}
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
            8
          </Text>{" "}
          /{" "}
          <Text as="span" color="#FF4E50">
            9
          </Text>{" "}
          /{" "}
          <Text as="span" color="white">
            22
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
                ? "lightBlueText"
                : kda < 5
                ? "terciary"
                : "#FF9B00"
            }
          >
            {kda}
          </Text>{" "}
          <Text as="span" color="white">
            KDA
          </Text>
        </Text>
        <Text fontSize="10px" fontWeight={300}>
          83 CS (4.3)
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
