import IronEmblem from "../assets/emblems/Rank=Iron.png";
import BronzeEmblem from "../assets/emblems/Rank=Bronze.png";
import SilverEmblem from "../assets/emblems/Rank=Silver.png";
import GoldEmblem from "../assets/emblems/Rank=Gold.png";
import PlatinumEmblem from "../assets/emblems/Rank=Platinum.png";
import EmeraldEmblem from "../assets/emblems/Rank=Emerald.png";
import DiamondEmblem from "../assets/emblems/Rank=Diamond.png";
import MasterEmblem from "../assets/emblems/Rank=Master.png";
import GrandmasterEmblem from "../assets/emblems/Rank=Grandmaster.png";
import ChallengerEmblem from "../assets/emblems/Rank=Challenger.png";

type Rank =
  | "IRON"
  | "BRONZE"
  | "SILVER"
  | "GOLD"
  | "PLATINUM"
  | "EMERALD"
  | "DIAMOND"
  | "MASTER"
  | "GRANDMASTER"
  | "CHALLENGER";

const rankEmblems: Record<Rank, string> = {
  IRON: IronEmblem,
  BRONZE: BronzeEmblem,
  SILVER: SilverEmblem,
  GOLD: GoldEmblem,
  PLATINUM: PlatinumEmblem,
  EMERALD: EmeraldEmblem,
  DIAMOND: DiamondEmblem,
  MASTER: MasterEmblem,
  GRANDMASTER: GrandmasterEmblem,
  CHALLENGER: ChallengerEmblem,
};

export default rankEmblems;
