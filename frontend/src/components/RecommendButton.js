import { api } from "../api/wavematchApi";
import { useState } from "react";

export default function RecommendButton() {
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleClick = async () => {
    try {
      const data = await api.recommend("Blinding My Vision", {
        save: true,
        playlist_name: "Vision Mix",
      });
      setResult(data);
    } catch (err) {
      setError(err.detail || "Request failed");
    }
  };

  return (
    <div>
      <button onClick={handleClick}>
        Get Recommendations
      </button>

      {error && <p>{error}</p>}

      {result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  );
}
