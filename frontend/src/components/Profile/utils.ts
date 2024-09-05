import DEFAULT_IMAGE from "../../assets/blue_bg.png";
import DEFAULT_PROFILE_IMG from "../../assets/Rank=Challenger.png";
import { SearchResponse } from "../../interfaces";

export const getChampionImageUrl = (
  championName: string | undefined
): string => {
  try {
    return new URL(
      `../../assets/centered/${championName}_1.jpg`,
      import.meta.url
    ).href;
  } catch (error) {
    return DEFAULT_IMAGE;
  }
};

export const getHeaderChampion = (
  data: SearchResponse | null
): string | undefined => {
  if (data && data.championStats.length > 0) {
    return data.championStats.reduce((max, champion) =>
      champion.gamesPlayed > max.gamesPlayed ? champion : max
    ).name;
  }
  return undefined;
};

export const getProfileIconId = (
  data: SearchResponse | null
): number | undefined => {
  if (data && data.profileIconId) {
    return data.profileIconId;
  }
  return undefined;
};
export const getProfileImgUrl = (profileIconId: number | undefined): string => {
  try {
    return new URL(
      `../../assets/img/profileicon/${profileIconId}.png`,
      import.meta.url
    ).href;
  } catch (error) {
    return DEFAULT_PROFILE_IMG;
  }
};
