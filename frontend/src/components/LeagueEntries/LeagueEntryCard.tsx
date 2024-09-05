import { Flex, Image, Text, Spacer } from "@chakra-ui/react";
import { CardTitle } from "../ui/CardTitle";

interface LeagueEntryCardProps {
  title: string;
  emblemUrl?: string;
  rank?: string;
  leaguePoints?: number;
  wins?: number;
  losses?: number;
  wr?: number;
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
  const isUnranked = !rank;

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
        direction={"row"}
        alignItems={"center"}
        height={"80px"}
        pl="15px"
        pr="10px"
        justifyContent={"space-between"}
      >
        {isUnranked ? (
          <Text fontSize="18px" fontWeight={600}>
            {title} - Unranked
          </Text>
        ) : (
          <>
            {emblemUrl && <Image src={emblemUrl} height={12} ml={3} mt={1} />}
            {/* Rank container */}
            <Flex ml={3} direction={"column"}>
              <Text fontSize="18px" fontWeight={600}>
                {rank}
              </Text>
              <Text fontSize="14px" color={"lightblueText"}>
                {leaguePoints} lp
              </Text>
            </Flex>
            <Spacer />
            {/* Winrate container */}
            <Flex mr={3} pt={3} direction={"column"} textAlign={"right"}>
              <Text fontSize="12px" fontWeight={600} color={"lightblueText"}>
                {wins}W {losses}L
              </Text>
              <Text fontSize="12px" fontWeight={600} color={"lightblueText"}>
                {wr}% Win Rate
              </Text>
            </Flex>
          </>
        )}
      </Flex>
    </Flex>
  );
}

export default LeagueEntryCard;
