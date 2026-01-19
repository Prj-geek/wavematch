import { useState } from "react";
import { api } from "../api/wavematchApi";

export default function MultiSearchBar({ onResults }) {
  const [input, setInput] = useState("");
  const [selected, setSelected] = useState([]);
  const [error, setError] = useState(null);

  const addSong = () => {
    if (!input.trim()) return;
    setSelected([...selected, input.trim()]);
    setInput("");
  };

  const removeSong = (name) => {
    setSelected(selected.filter((s) => s !== name));
  };

  const recommend = async () => {
    if (selected.length < 2) {
      setError("Select at least 2 songs");
      return;
    }

    try {
      const data = await api.recommendMulti(selected);
      onResults(data);
      setError(null);
    } catch (err) {
      setError(err.detail || "Failed to recommend");
    }
  };

  return (
    <div>
      <input
        placeholder="Enter song name and press Add"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button onClick={addSong}>Add</button>

      <div>
        {selected.map((s) => (
          <span key={s} style={{ marginRight: "0.5rem" }}>
            {s}
            <button onClick={() => removeSong(s)}>✕</button>
          </span>
        ))}
      </div>

      <button onClick={recommend}>Generate Playlist</button>

      {error && <p>{error}</p>}
    </div>
  );
}
<div className="chips">
  {selected.map((s) => (
    <span className="chip" key={s}>
      {s}
      <button onClick={() => removeSong(s)}>×</button>
    </span>
  ))}
</div>
{error && <p className="error">{error}</p>}
