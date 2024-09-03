import { Flex, Image, Text, Spacer, Box } from "@chakra-ui/react";

interface CardTitleProps {
  text: string;
  fontSize?: string;
  mt?: number;
  ml?: number;
  mr?: number;
  mb?: number;
}

export function CardTitle({
  text,
  fontSize = "15px",
  mt = 4,
  ml = 4,
  mr = 4,
  mb = 0,
}: CardTitleProps) {
  return (
    <Flex
      //   bgColor={"#F251FA"}
      direction={"row"}
      alignItems="center"
      mt={mt}
      ml={ml}
      mr={mr}
      mb={mb}
    >
      <Box
        h="1.4rem"
        w="2px"
        bgColor={"#3273FA"}
        borderRadius={3}
        marginRight={3}
      />
      <Text fontSize={fontSize} fontWeight={600}>
        {text}
      </Text>
    </Flex>
  );
}
