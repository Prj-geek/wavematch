import { useEffect, useState } from "react";
import { api } from "../api/wavematchApi";

export default function Playlists() {
  const [playlists, setPlaylists] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function load() {
      try {
        const data = await api.playlists();
        setPlaylists(data);
      } catch (err) {
        setError(err.detail || "Failed to load playlists");
      }
    }
    load();
  }, []);

  if (error) return <p>{error}</p>;
  if (!playlists.length) return <p>No playlists yet</p>;

  return (
    <div>
      <h3>My Playlists</h3>
      {playlists.map((pl) => (
        <div key={pl.id} style={{ marginBottom: "1rem" }}>
          <strong>{pl.name}</strong>
          <ul>
            {pl.data.recommendations.map((s, i) => (
              <li key={i}>
                {s.track_name} — {s.artist_name} ({s.similarity.toFixed(2)})
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}
