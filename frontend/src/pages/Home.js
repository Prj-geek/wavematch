import { useState } from "react";
import Login from "../components/Login";
import Protected from "../components/Protected";
import SearchBar from "../components/SearchBar";
import MultiSearchBar from "../components/MultiSearchBar";
import RecommendationList from "../components/RecommendationList";
import Playlists from "../components/Playlists";

export default function Home() {
  const [recommendations, setRecommendations] = useState([]);

  return (
    <div className="container">
      <h1>WaveMatch</h1>

      <Login />

      <Protected>
        <h3>Single Song</h3>
        <SearchBar onResults={setRecommendations} />

        <h3>Playlist Seeds</h3>
        <MultiSearchBar onResults={setRecommendations} />

        <RecommendationList recommendations={recommendations} />
        <Playlists />
      </Protected>
    </div>
  );
}
