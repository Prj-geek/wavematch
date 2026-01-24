import { useState } from "react";
import { api } from "../api/wavematchApi";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  const handleLogin = async () => {
    try {
      const data = await api.login(username, password);
      localStorage.setItem("token", data.access_token);
      window.location.reload(); // simplest way
    } catch {
      setError("Login failed");
    }
  };

  return (
    <div>
      <input
        placeholder="username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Login</button>
      {error && <p>{error}</p>}
    </div>
  );
}
