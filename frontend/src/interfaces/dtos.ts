export interface LeagueEntry {
  queueType: string;
  tier: string;
  rank: string;
  leaguePoints: number;
  wins: number;
  losses: number;
  id: number;
  accountId: number;
}

export interface Participant {
  champion_id: number;
  champion_name: string;
  riot_id_game_name: string;
  riot_id_tagline: string;
  team_id: number;
  team_position: string;
  id: number;
  match_id: number;
}
export interface Match {
  match_id: string;
  game_creation: number;
  game_duration: number;
  game_end_timestamp: number;
  game_mode: string;
  game_start_timestamp: number;
  game_type: string;
  game_version: string;
  queue_id: number;
  assists: number;
  champ_level: number;
  champion_id: number;
  champion_name: string;
  deaths: number;
  gold_earned: number;
  individual_position: string;
  item_0: number;
  item_1: number;
  item_2: number;
  item_3: number;
  item_4: number;
  item_5: number;
  item_6: number;
  kills: number;
  lane: string;
  perk_0: number;
  perk_1: number;
  puuid: string;
  riot_id_game_name: string;
  riot_id_tag_line: string;
  summoner_1_id: number;
  summoner_2_id: number;
  summoner_id: string;
  team_id: number;
  team_position: string;
  total_damage_dealt_to_champions: number;
  total_minions_killed: number;
  vision_score: number;
  wards_placed: number;
  win: boolean;
  id: number;
  account_id: number;
  participants: Participant[];
}

export interface ChampionStats {
  name: string;
  gamesPlayed: number;
  killAvg: number;
  deathAvg: number;
  assistAvg: number;
  kda: number;
  wins: number;
  losses: number;
  winrate: number;
  id: number;
  accountId: number;
}

export interface Response {
  puuid: string;
  summonerId: string;
  accountId: string;
  gameName: string;
  tagLine: string;
  profileIconId: number;
  summonerLevel: number;
  lastUpdate: number;
  id: number;
  leagueEntries: LeagueEntry[];
  matches: Match[];
  championStats: ChampionStats[];
}
