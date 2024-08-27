import { Box } from "@chakra-ui/react";

type LevelBadgeProps = {
  level: number;
  borderColor: string;
};

function LevelBadge({ level, borderColor }: LevelBadgeProps) {
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

export default LevelBadge;
