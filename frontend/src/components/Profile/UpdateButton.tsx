import { Button, Spinner } from "@chakra-ui/react";

interface UpdateButtonProps {
  onUpdate: () => void;
  isLoading: boolean;
}

function UpdateButton({ onUpdate, isLoading }: UpdateButtonProps) {
  return (
    <Button
      mt={1}
      mb={4}
      bgColor={"terciary"}
      borderRadius={3}
      color={"white"}
      width={"130px"}
      _hover={{ bg: "#1E2B5E" }}
      onClick={onUpdate}
      isDisabled={isLoading}
    >
      {isLoading ? <Spinner size="md" color="orangeText" /> : "Update"}
    </Button>
  );
}
export default UpdateButton;
