import Login from "../components/Login";
import Protected from "../components/Protected";
import RecommendButton from "../components/RecommendButton";
import Playlists from "../components/Playlists";

export default function Home() {
  return (
    <div className="container">
      <h1>WaveMatch</h1>

      <Login />

      <Protected>
        <RecommendButton />
        <Playlists />
      </Protected>
    </div>
  );
}
