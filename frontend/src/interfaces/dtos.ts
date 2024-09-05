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
  championId: number;
  championName: string;
  riotIdGameName: string;
  riotIdTagline: string;
  teamId: number;
  teamPosition: string;
  id: number;
  matchId: number;
}

export interface Match {
  matchId: string;
  gameCreation: number;
  gameDuration: number;
  gameEndTimestamp: number;
  gameMode: string;
  gameDtartTimestamp: number;
  gameType: string;
  gameVersion: string;
  queueId: number;
  assists: number;
  champLevel: number;
  championId: number;
  championName: string;
  deaths: number;
  goldEarned: number;
  individualPosition: string;
  item0: number;
  item1: number;
  item2: number;
  item3: number;
  item4: number;
  item5: number;
  item6: number;
  kills: number;
  lane: string;
  perk0: number;
  perk1: number;
  puuid: string;
  riotIdGameName: string;
  riotIdTagLine: string;
  summoner1Id: number;
  summoner2Id: number;
  summonerId: string;
  teamId: number;
  teamPosition: string;
  totalDamageDealtToChampions: number;
  totalMinionsKilled: number;
  visionScore: number;
  wardsPlaced: number;
  win: boolean;
  id: number;
  accountId: number;
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

export interface SearchResponse {
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
