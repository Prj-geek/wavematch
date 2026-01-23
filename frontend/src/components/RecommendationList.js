import { useState } from "react";
import SongCard from "./SongCard";

export default function RecommendationList({ recommendations }) {
  const [order, setOrder] = useState("desc");

  if (!recommendations || !recommendations.length) {
    return (
  <p className="muted">
    Search for a song or select multiple songs to get recommendations.
  </p>
);

  }

  const sorted = [...recommendations].sort((a, b) => {
    if (order === "desc") {
      return b.similarity - a.similarity;
    }
    return a.similarity - b.similarity;
  });

  return (
    <div className="recommendations">
      <div style={{ marginBottom: "0.5rem" }}>
        <label style={{ marginRight: "0.5rem" }}>Sort by similarity:</label>
        <select
          value={order}
          onChange={(e) => setOrder(e.target.value)}
        >
          <option value="desc">High → Low</option>
          <option value="asc">Low → High</option>
        </select>
      </div>

      {sorted.map((song, index) => (
        <SongCard key={index} song={song} />
      ))}
    </div>
  );
}
