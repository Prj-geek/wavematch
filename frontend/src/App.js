import { AuthProvider } from "./context/AuthContext";
import Home from "./pages/Home";
import "./styles/main.css";

function App() {
  return (
    <AuthProvider>
      <Home />
    </AuthProvider>
  );
}

export default App;
