import { Box, Image, useTheme } from "@chakra-ui/react";

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

// LevelBadge
type LevelBadgeProps = {
  level: number;
  borderColor: string;
};

export function LevelBadge({ level, borderColor }: LevelBadgeProps) {
  return (
    <Box
      position="absolute"
      top="-14%"
      left="50%"
      transform="translateX(-50%)"
      width="35%"
      height="20%"
      bg="background"
      borderRadius="4"
      border={`1px solid ${borderColor}`}
      fontSize="12px"
      fontWeight="700"
      display="flex"
      alignItems="center"
      justifyContent="center"
    >
      {level}
    </Box>
  );
}
