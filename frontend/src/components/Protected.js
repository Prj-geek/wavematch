import { useAuth } from "../context/AuthContext";

export default function Protected({ children }) {
  const { token } = useAuth();

  if (!token) {
    return <p>Please log in</p>;
  }

  return children;
}
