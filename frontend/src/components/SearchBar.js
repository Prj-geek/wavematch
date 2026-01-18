import { useState } from "react";
import { api } from "../api/wavematchApi";

export default function SearchBar({ onResults }) {
  const [query, setQuery] = useState("");
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    if (!query.trim()) return;

    try {
      const data = await api.recommend(query);
      onResults(data);
      setError(null);
    } catch (err) {
      setError(err.detail || "Song not found");
    }
  };

  return (
    <div>
      <input
        placeholder="Enter song name"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch}>Recommend</button>

      {error && <p>{error}</p>}
    </div>
  );
}
