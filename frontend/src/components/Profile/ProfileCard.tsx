import { Box, Button, Text, useTheme } from "@chakra-ui/react";
import ProfileImage from "./ProfileImage";
import { SearchResponse } from "../../interfaces";
import {
  getHeaderChampion,
  getChampionImageUrl,
  getProfileImgUrl,
  getProfileIconId,
} from "./utils";

interface ProfileCardProps {
  data: SearchResponse | null;
  imageAlt?: string;
  bgImage?: string;
}

export function ProfileCard({ data }: ProfileCardProps) {
  const theme = useTheme();
  const terciaryColor = theme.colors.terciary;

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
        <Button
          mt={1}
          mb={4}
          bgColor={terciaryColor}
          borderRadius={3}
          color={"white"}
          width={"130px"}
          _hover={{ bg: { terciaryColor } }}
        >
          Update
        </Button>
      </Box>
    </Box>
  );
}
