import { Flex } from "@chakra-ui/react";

type MatchCardProps = {
  bgColor: string;
};
export function MatchCard({ bgColor }: MatchCardProps) {
  return (
    <Flex
      bgColor={bgColor}
      direction={"row"}
      marginInline={3}
      marginTop={1}
      h={"100px"}
      borderRadius={3}
    ></Flex>
  );
}
