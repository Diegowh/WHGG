import { useState, useEffect, useRef } from "react";
import { SearchResponse } from "../interfaces";

const BASE_URL = "https://whgg.onrender.com/lol/profile/";

interface SearchParams {
  gameName: string;
  tagLine: string;
  server: string;
}

export function useSearch() {
  const [error, setError] = useState<Error | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState<SearchResponse | null>(null);

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
      const data: SearchResponse = await response.json();
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

  useEffect(() => {
    if (result !== null) {
      console.log("Result: ", result);
    }
  }, [result]);

  return { handleSearch, error, isLoading, result };
}
