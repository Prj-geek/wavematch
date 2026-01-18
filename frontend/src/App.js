import Login from "./components/Login";
import Protected from "./components/Protected";
import RecommendButton from "./components/RecommendButton";
import Playlists from "./components/Playlists";
import { AuthProvider } from "./context/AuthContext";

function App() {
  return (
    <AuthProvider>
      <Login />
      <Protected>
        <RecommendButton />
        <Playlists />
      </Protected>
    </AuthProvider>
  );
}

export default App;
