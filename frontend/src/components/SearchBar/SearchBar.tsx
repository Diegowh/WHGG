import { useState } from "react";
import {
  Box,
  Input,
  InputGroup,
  InputRightElement,
  Select,
  IconButton,
  useTheme,
} from "@chakra-ui/react";
import { Search2Icon } from "@chakra-ui/icons";
import { useSearch } from "../../hooks/useSearch";

const servers = [
  "NA",
  "EUW",
  "EUNE",
  "OCE",
  "KR",
  "JP",
  "BR",
  "LAN",
  "LAS",
  "RU",
  "TR",
  "SG",
  "PH",
  "TW",
  "VN",
  "TH",
];
type OptionProps = {
  value: string;
};

function Option({ value }: OptionProps) {
  return (
    <option
      style={{ backgroundColor: "#2D3748", color: "white" }}
      value={value}
    >
      {value}
    </option>
  );
}

function SearchBar() {
  const [query, setQuery] = useState("");
  const [server, setServer] = useState("EUW");

  const { handleSearch, error, isLoading, result } = useSearch();

  const theme = useTheme();
  const secondaryColor = theme.colors.secondary;
  const placeholderText = `Game name + #${server}`;

  const onSearch = () => {
    const [gameName, tagLine] = query.split("#");
    handleSearch({ gameName, tagLine, server });
    console.log("Result: ", result);
  };

  return (
    <Box
      display="flex"
      alignItems="center"
      bg={secondaryColor}
      p={4}
      borderRadius={20}
    >
      <Select
        value={server}
        onChange={(e) => setServer(e.target.value)}
        width="120px"
        mr={2}
        bg="background"
        color="text"
        _hover={{ bg: "gray.600" }}
        _focus={{ boxShadow: "none" }}
        borderRadius="md"
      >
        {servers.map((server) => (
          <Option key={server} value={server} />
        ))}
      </Select>

      <InputGroup>
        <Input
          placeholder={placeholderText}
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          bg="white"
          color="background"
        />
        <InputRightElement pr="3">
          <IconButton
            aria-label="Search"
            icon={<Search2Icon />}
            borderRadius={20}
            height="80%"
            onClick={onSearch}
            bg="background"
            color="white"
            _hover={{ bg: secondaryColor }}
            isLoading={isLoading}
          />
        </InputRightElement>
      </InputGroup>
    </Box>
  );
}

export default SearchBar;
