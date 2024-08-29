import { useState } from "react";
import {
  Box,
  BoxProps,
  Input,
  InputGroup,
  InputRightElement,
  Select,
  IconButton,
  useTheme,
  InputProps,
  SelectProps,
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
      style={{ backgroundColor: "#0D0D28", color: "#CDDCFE" }}
      value={value}
    >
      {value}
    </option>
  );
}
interface SearchBarProps extends BoxProps {
  inputProps?: InputProps;
  selectProps?: SelectProps;
  width?: string | number;
  height?: string | number;
}

function SearchBar({
  // width = "100%",
  // height = "25%",
  inputProps,
  selectProps,
  ...boxProps
}: SearchBarProps) {
  const [query, setQuery] = useState("");
  const [server, setServer] = useState("EUW");

  const { handleSearch, error, isLoading, result } = useSearch();

  const theme = useTheme();
  const secondaryColor = theme.colors.secondary;
  const placeholderText = `Game name + #${server}`;

  const onSearch = () => {
    const [gameName, tagLine] = query.split("#");
    handleSearch({ gameName, tagLine, server });
  };

  return (
    <Box
      display="flex"
      alignItems="center"
      bg="#0D0D28"
      borderRadius={5}
      height={"40px"}
      {...boxProps}
    >
      <Select
        value={server}
        onChange={(e) => setServer(e.target.value)}
        width="90px"
        border="none"
        mr={0}
        bg={"#0D0D28"}
        color="#CDDCFE"
        _hover={{ bg: "#0D0D28" }}
        _focus={{ boxShadow: "none" }}
        borderRadius="md"
        // marginLeft="3"
      >
        {servers.map((server) => (
          <Option key={server} value={server} />
        ))}
      </Select>

      <InputGroup flex="1" ml="0">
        <Input
          placeholder={placeholderText}
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          bg={"#0D0D28"}
          color="white"
          borderRadius="md"
          border="none"
          focusBorderColor={secondaryColor}
        />
        <InputRightElement pr="3">
          <IconButton
            aria-label="Search"
            icon={<Search2Icon />}
            borderRadius="md"
            // height="80%"
            onClick={onSearch}
            bg={"#0D0D28"}
            color="white"
            _hover={{ bg: "#0D0D28" }}
            isLoading={isLoading}
            border="none"
          />
        </InputRightElement>
      </InputGroup>
    </Box>
  );
}

export default SearchBar;
