import { Flex, Text } from "@chakra-ui/react";
import { ImageTile } from "../ui/ImageTile";
import { Participant } from "../../interfaces";
import { getChampionTileUrl } from "../../utils/utils";

interface ParticipantRowProps {
  participant: Participant;
}
export function ParticipantRow({ participant }: ParticipantRowProps) {
  return (
    <Flex direction={"row"} pt={"1px"}>
      <ImageTile
        img={getChampionTileUrl(participant.championName)}
        boxSize="16px"
      />

      <Text
        fontSize="11px"
        fontWeight={300}
        pl={1}
        alignSelf={"center"}
        // marginLeft={"10px"}
        isTruncated
        maxWidth="60px"
        color="lightblueText"
        title={`${participant.riotIdGameName}#${participant.riotIdTagline}`}
      >
        {`${participant.riotIdGameName}`}
      </Text>
    </Flex>
  );
}
