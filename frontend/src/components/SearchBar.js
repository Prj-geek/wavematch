import { useState } from "react";
import { api } from "../api/wavematchApi";

export default function SearchBar({ onResults }) {
  const [query, setQuery] = useState(
    localStorage.getItem("last_query") || ""
  );
  const [limit, setLimit] = useState(10);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    localStorage.setItem("last_query", query);
    if (!query.trim()) return;

    setLoading(true);
    try {
      const data = await api.recommend(query, { limit });
      onResults(data);
      setError(null);
    } catch (err) {
      setError(err.detail || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <input
        placeholder="Enter song name"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        disabled={loading}
      />

      <select
        value={limit}
        onChange={(e) => setLimit(Number(e.target.value))}
        disabled={loading}
      >
        <option value={5}>5</option>
        <option value={10}>10</option>
        <option value={20}>20</option>
      </select>

      <button onClick={handleSearch} disabled={loading}>
        {loading ? "Loading..." : "Recommend"}
      </button>

      {error && <p className="error">{error}</p>}
    </div>
  );
}
