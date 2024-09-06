import { Box, Text } from "@chakra-ui/react";
import ProfileImage from "./ProfileImage";
import { SearchResponse } from "../../interfaces";
import {
  getHeaderChampion,
  getChampionImageUrl,
  getProfileImgUrl,
  getProfileIconId,
} from "./utils";
import UpdateButton from "./UpdateButton";
interface ProfileCardProps {
  data: SearchResponse | null;
  onUpdate: () => void;
  isLoading: boolean;
  imageAlt?: string;
  bgImage?: string;
}

export function ProfileCard({ data, onUpdate, isLoading }: ProfileCardProps) {
  const profileIconId = getProfileIconId(data);
  const imageSrc = getProfileImgUrl(profileIconId);
  const level = data?.summonerLevel ?? 0;
  const gameName = data?.gameName ?? "null";
  const tagLine = data?.tagLine ?? "null";
  const headerChampionName = getHeaderChampion(data);
  const headerChampionUrl = getChampionImageUrl(headerChampionName);

  return (
    <Box
      bgColor={"background"}
      display={"flex"}
      position={"relative"}
      alignItems={"center"}
      justifyContent={"flex-start"}
      pt={4}
      pb={4}
      pr={4}
      pl={2}
      _before={{
        content: '""',
        position: "absolute",
        top: "0%",
        right: "0%",
        bottom: "0%",
        left: "0%",
        backgroundImage: `linear-gradient(to left, rgba(0, 0, 0, 0), rgba(7, 7, 32, 1)80%), url(${headerChampionUrl})`,

        backgroundPosition: "100% 25%",
        backgroundRepeat: "no-repeat",
        backgroundSize: "80%",
        opacity: 0.6,
      }}
    >
      <ProfileImage src={imageSrc} level={level} />
      <Box display="flex" flexDirection="column" alignItems="start">
        <Text
          // as="b"
          // backgroundColor={"tomato"}
          fontSize="3xl"
          position="relative"
          pt={6}
        >
          <Text as="span" color="white" fontWeight={600}>
            {gameName}
          </Text>{" "}
          <Text as="span" color="lightblueText">
            #{tagLine}
          </Text>
        </Text>
        <UpdateButton onUpdate={onUpdate} isLoading={isLoading} />
      </Box>
    </Box>
  );
}
