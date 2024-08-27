import "./App.css";
import ProfileImage from "./components/ProfileImage";
// import UpdateButton from "./components/UpdateButton";
import FiddlesticksIcon from "./assets/static/6022.png";

function App() {
  const level: number = 534;
  const imageSrc: string = FiddlesticksIcon;
  const imageAlt: string = "Fiddlesticks";

  return <ProfileImage src={imageSrc} alt={imageAlt} level={level} />;
}

export default App;
