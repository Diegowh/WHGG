import { Flex, Text, Image, Box } from "@chakra-ui/react";
import { ImageTile } from "../ui/ImageTile";

interface ParticipantRowProps {
  img: string;
  riotId: string;
}
export function ParticipantRow({ img, riotId }: ParticipantRowProps) {
  return (
    <Flex direction={"row"} pt={"1px"}>
      <ImageTile img={img} boxSize="16px" />

      <Text
        fontSize="11px"
        fontWeight={300}
        alignSelf={"center"}
        // marginLeft={"10px"}
        isTruncated
        maxWidth="60px"
        color="ligthBlueText"
      >
        {riotId}
      </Text>
    </Flex>
  );
}
