import { useState } from "react";
import { api } from "../api/wavematchApi";

export default function SearchBar({ onResults }) {
  const [query, setQuery] = useState("");
  const [limit, setLimit] = useState(10);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    if (!query.trim()) return;

    try {
      const data = await api.recommend(query, { limit });
      onResults(data);
      setError(null);
    } catch (err) {
      setError(err.detail || "Something went wrong");
    }
  };

  return (
    <div>
      <input
        placeholder="Enter song name"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <select
        value={limit}
        onChange={(e) => setLimit(Number(e.target.value))}
      >
        <option value={5}>5</option>
        <option value={10}>10</option>
        <option value={20}>20</option>
      </select>

      <button onClick={handleSearch}>Recommend</button>

      {error && <p className="error">{error}</p>}
    </div>
  );
}
