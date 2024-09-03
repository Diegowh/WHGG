import { Flex, Image, Text, Spacer, Box } from "@chakra-ui/react";
import { CardTitle } from "../ui/CardTitle";

interface LeagueEntryCardProps {
  title: string;
  emblemUrl: string;
  rank: string;
  leaguePoints: number;
  wins: number;
  losses: number;
  wr: number;
}

function LeagueEntryCard({
  title,
  emblemUrl,
  rank,
  leaguePoints,
  wins,
  losses,
  wr,
}: LeagueEntryCardProps) {
  return (
    <Flex
      bgColor={"secondary"}
      w="100%"
      h="120px"
      mb={3}
      direction={"column"}
      borderRadius={"3px"}
    >
      {/* Card Title */}
      <CardTitle text={title} />
      {/* Contenido */}
      <Flex
        // bgColor="red"
        direction={"row"}
        alignItems={"center"}
        height={"80px"}
        pl="15px"
        pr="10px"
      >
        <Image src={emblemUrl} height={12} ml={3} mt={1} />
        {/* Rank container */}
        <Flex ml={3} direction={"column"}>
          <Text fontSize="18px" fontWeight={600}>
            {rank}
          </Text>
          <Text fontSize="14px" color={"#C1D0F2"}>
            {leaguePoints} lp
          </Text>
        </Flex>
        <Spacer />
        {/* Winrate container */}
        <Flex mr={3} pt={3} direction={"column"} textAlign={"right"}>
          <Text fontSize="12px" fontWeight={600} color={"#C1D0F2"}>
            {wins}W {losses}L
          </Text>
          <Text fontSize="12px" fontWeight={600} color={"#C1D0F2"}>
            {wr}% Win Rate
          </Text>
        </Flex>
      </Flex>
    </Flex>
  );
}

export default LeagueEntryCard;
