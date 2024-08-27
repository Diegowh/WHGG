import { Box, Image, useTheme } from "@chakra-ui/react";
import LevelBadge from "./LevelBadge";

type ProfileImageProps = {
  src: string;
  alt: string;
  level: number;
};
function ProfileImage({ src, alt, level }: ProfileImageProps) {
  const theme = useTheme();
  const borderColor = theme.colors.border;

  return (
    <Box position="relative" display="inline-block" margin="1rem">
      <Image
        src={src}
        alt={alt}
        width="100px"
        height="100px"
        border={`2px solid ${borderColor}`}
        borderRadius="6"
        padding="2px"
      />
      <LevelBadge level={level} borderColor={borderColor} />
    </Box>
  );
}

export default ProfileImage;
