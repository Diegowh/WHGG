import "./App.css";
import ProfileImage from "./components/Profile/ProfileImage";
// import UpdateButton from "./components/UpdateButton";
import FiddlesticksIcon from "./assets/6022.png";
import SearchBar from "./components/SearchBar/SearchBar";
import { Box } from "@chakra-ui/react";
import Home from "./pages/Home";

function App() {
  const level: number = 534;
  const imageSrc: string = FiddlesticksIcon;
  const imageAlt: string = "Fiddlesticks";
  function handleSearch(params: { query: string; server: string }) {
    console.log("Search query:", params.query);
    console.log("Selected server:", params.server);
  }

  return (
    // <Box p={5}>
    //   <SearchBar onSearch={handleSearch} />
    //   <ProfileImage src={imageSrc} alt={imageAlt} level={level} />
    // </Box>
    <Home onSearch={handleSearch} />
  );
}

export default App;
