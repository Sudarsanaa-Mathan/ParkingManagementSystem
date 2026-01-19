const API_BASE = "http://localhost:8000";

export async function login(username, password) {
  const formData = new URLSearchParams();
  formData.append("username", username);
  formData.append("password", password);

  const res = await fetch(`${API_BASE}/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
       "Accept": "application/json",
    },
    body: formData.toString(),
  });

  const data = await res.json();

  if (!res.ok) {
    throw new Error(data.detail || "Login failed");
  }

  // store token + role
  localStorage.setItem("token", data.access_token);
  localStorage.setItem("role", data.role);

  return data;
}

export function logout() {
  localStorage.clear();
}

export function getRole() {
  return localStorage.getItem("role");
}

export function getToken() {
  return localStorage.getItem("token");
}
