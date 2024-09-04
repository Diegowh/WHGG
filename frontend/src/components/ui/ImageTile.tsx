import { Image, Flex } from "@chakra-ui/react";

interface ImageTileProps {
  img: string;
  boxSize?: string;
}

export function ImageTile({ img, boxSize = "35px" }: ImageTileProps) {
  return (
    <Flex
      overflow="hidden"
      width="fit-content"
      height={"fit-content"}
      alignItems="center"
      justifyContent="center"
      borderRadius={"3px"}
    >
      <Image
        src={img}
        boxSize={boxSize}
        objectFit="cover"
        transform="scale(1.2)"
      />
    </Flex>
  );
}
