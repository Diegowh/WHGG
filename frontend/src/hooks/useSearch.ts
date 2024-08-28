import { useState, useEffect, useRef } from "react";

const BASE_URL = "http://localhost:8000/lol/profile/";

interface SearchParams {
  gameName: string;
  tagLine: string;
  server: string;
}
interface SearchResult {}

export function useSearch() {
  const [error, setError] = useState<Error | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState<SearchResult | null>(null);

  const abortControllerRef = useRef<AbortController | null>(null);

  async function handleSearch({ gameName, tagLine, server }: SearchParams) {
    abortControllerRef.current?.abort();
    abortControllerRef.current = new AbortController();

    setIsLoading(true);

    try {
      const response = await fetch(
        `${BASE_URL}${server}/${gameName}-${tagLine}/`,
        {
          signal: abortControllerRef.current.signal,
        }
      );
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data: SearchResult = await response.json();
      setResult(data);
    } catch (e: any) {
      if (e.name === "AbortError") {
        console.log("Request aborted");
        return;
      }

      setError(e);
    } finally {
      setIsLoading(false);
    }
  }
  return { handleSearch, error, isLoading, result };
}
