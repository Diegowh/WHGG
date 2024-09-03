import { Box, Button, Text, useTheme } from "@chakra-ui/react";
import ProfileImage from "./ProfileImage";
import FiddlesticksIcon from "../../assets/6022.png";
import FiddlesticksBackground from "../../assets/fiddlesticks_bg.jpg";

type ProfileCardProps = {
  level?: number;
  imageSrc?: string;
  imageAlt?: string;
  bgImage?: string;
};

export function ProfileCard({
  level = 534,
  imageSrc = FiddlesticksIcon,
  imageAlt = "Fiddlesticks",
  bgImage = FiddlesticksBackground,
}: ProfileCardProps) {
  //   const level: number = 534;
  //   const imageSrc: string = FiddlesticksIcon;
  //   const imageAlt: string = "Fiddlesticks";
  //   const bgImage: string = FiddlesticksBackground;

  const theme = useTheme();
  const terciaryColor = theme.colors.terciary;
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
        backgroundImage: `linear-gradient(to left, rgba(0, 0, 0, 0), rgba(7, 7, 32, 1)80%), url(${bgImage})`,

        backgroundPosition: "100% 25%",
        backgroundRepeat: "no-repeat",
        backgroundSize: "80%",
        opacity: 0.6,
      }}
    >
      <ProfileImage src={imageSrc} alt={imageAlt} level={level} />
      <Box display="flex" flexDirection="column" alignItems="start">
        <Text
          // as="b"
          // backgroundColor={"tomato"}
          fontSize="3xl"
          position="relative"
          pt={6}
          fontFamily={"Barlow, sans-serif"}
        >
          wallhack #1312
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
