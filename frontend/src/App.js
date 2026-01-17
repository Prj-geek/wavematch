import Login from "./components/Login";
import Protected from "./components/Protected";
import { AuthProvider } from "./context/AuthContext";

function App() {
  return (
    <AuthProvider>
      <Login />
      <Protected>
        <p>You are logged in</p>
      </Protected>
    </AuthProvider>
  );
}

export default App;
