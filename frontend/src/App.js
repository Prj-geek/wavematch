import RecommendButton from "./components/RecommendButton";
import Protected from "./components/Protected";
import Login from "./components/Login";
import { AuthProvider } from "./context/AuthContext";

function App() {
  return (
    <AuthProvider>
      <Login />
      <Protected>
        <RecommendButton />
      </Protected>
    </AuthProvider>
  );
}

export default App;
