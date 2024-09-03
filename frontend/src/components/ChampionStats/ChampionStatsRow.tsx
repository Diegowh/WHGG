import { Flex, Image, Box } from "@chakra-ui/react";

interface ChampionStatsRowProps {
  img: string;
}
function ChampionStatsRow({ img }: ChampionStatsRowProps) {
  return (
    <Flex
      bgColor={"secondary"}
      height={"59px"}
      direction={"row"}
      padding={3}
      marginBottom={"1px"}
    >
      <Box overflow="hidden" width="fit-content">
        <Image
          src={img}
          boxSize="35px"
          objectFit="cover"
          transform="scale(1.2)"
        />
      </Box>
    </Flex>
  );
}

export default ChampionStatsRow;
