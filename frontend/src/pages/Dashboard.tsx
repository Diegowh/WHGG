import { Box, Button, Text, useTheme } from "@chakra-ui/react";
import HeaderBar from "../components/HeaderBar";
import ProfileImage from "../components/Profile/ProfileImage";
import FiddlesticksIcon from "../assets/6022.png";
import FiddlesticksBackground from "../assets/fiddlesticks_bg.jpg";

function Dashboard() {
  const level: number = 534;
  const imageSrc: string = FiddlesticksIcon;
  const imageAlt: string = "Fiddlesticks";
  const bgImage: string = FiddlesticksBackground;

  const theme = useTheme();
  const secondaryColor = theme.colors.secondary;
  const terciaryColor = theme.colors.terciary;
  return (
    <Box display="flex" flexDirection="column" height="100vh">
      <HeaderBar />
      <Box
        overflow="auto"
        flex="1"
        display="flex"
        justifyContent="center"
        mt="5px"
      >
        <Box
          //bgColor="purple"
          borderRadius={5}
          width="1000px"
        >
          <Box
            // bgColor={"tomato"}
            display={"flex"}
            position={"relative"}
            alignItems={"center"}
            justifyContent={"flex-start"}
            p={4}
            _before={{
              content: '""',
              position: "absolute",
              top: "0%",
              right: "0%",
              bottom: "0%",
              left: "0%",
              backgroundImage: `linear-gradient(to left, rgba(0, 0, 0, 0), rgba(0, 0, 0, 1)), url(${bgImage})`,

              backgroundPosition: "100% 25%",
              backgroundRepeat: "no-repeat",
              backgroundSize: "100%",
              opacity: 0.3,
              zIndex: -1,
            }}
          >
            <ProfileImage src={imageSrc} alt={imageAlt} level={level} />
            <Box
              // bgColor={"tomato"}
              display="flex"
              flexDirection="column"
              alignItems="start"
            >
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
                width={150}
                _hover={{ bg: { terciaryColor } }}
              >
                Update
              </Button>
            </Box>
          </Box>
        </Box>
      </Box>
    </Box>
  );
}

export default Dashboard;
