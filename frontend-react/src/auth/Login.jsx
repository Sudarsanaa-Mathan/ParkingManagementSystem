import { useState } from "react";
import { login } from "./authService";
import { useNavigate } from "react-router-dom";
import "./Login.css";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  async function handleLogin(e) {
    e.preventDefault();
    setError("");

    try {
      const data = await login(username, password);

      // route by role
      if (data.role === "ADMIN") {
        navigate("/admin");
      } else if (data.role === "SECURITY") {
        navigate("/security");
      } else {
        setError("Unknown role");
      }
    } catch (err) {
      setError(err?.detail || err?.message || JSON.stringify(err));

    }
  }

  return (
    <div className="login-container">
       <h2>Smart Parking Login</h2>

      <form className="login-card" onSubmit={handleLogin}>
        

        <input
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">Login</button>
      </form>
        {error && <p className="error">{error}</p>}
      
    </div>
  );
}
