import DEFAULT_IMAGE from "../assets/blue_bg.png";

export function toCamelCase(str: string): string {
  return str
    .replace(/_(\d+)/g, (_, number) => number) // Elimina las barras bajas antes de números
    .replace(/_([a-z])/g, (_, letter) => letter.toUpperCase()) // Convierte a camelCase
    .replace(/^([a-z])/, (match) => match.toLowerCase()); // Asegura que la primera letra esté en minúscula
}

export function transformObjectKeys(obj: any): any {
  if (Array.isArray(obj)) {
    return obj.map((item) => transformObjectKeys(item));
  } else if (obj !== null && typeof obj === "object") {
    return Object.keys(obj).reduce((acc, key) => {
      const camelCaseKey = toCamelCase(key);
      acc[camelCaseKey] = transformObjectKeys(obj[key]);
      return acc;
    }, {} as any);
  }
  return obj;
}

export function getWinrate(w: number, l: number): number {
  const totalGames = w + l;
  if (totalGames === 0) {
    return 0;
  }
  return Math.round((w / totalGames) * 100);
}

export function capitalize(str: string): string {
  if (str.length === 0) return str;
  return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

export const getChampionTileUrl = (
  championName: string | undefined
): string => {
  try {
    return new URL(`../assets/tiles/${championName}.png`, import.meta.url).href;
  } catch (error) {
    return DEFAULT_IMAGE;
  }
};
