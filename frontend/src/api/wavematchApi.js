const BASE_URL = "http://127.0.0.1:8000";

export function getToken() {
  return localStorage.getItem("access_token");
}

export function setToken(token) {
  localStorage.setItem("access_token", token);
}

export function clearToken() {
  localStorage.removeItem("access_token");
}

async function request(path, options = {}) {
  const token = getToken();

  const headers = {
    "Content-Type": "application/json",
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
    ...options.headers,
  };

  const res = await fetch(`${BASE_URL}${path}`, {
    ...options,
    headers,
  });

  if (!res.ok) {
    const err = await res.json();
    throw err;
  }

  return res.json();
}

export const api = {
  login: async (username, password) => {
  const body = new URLSearchParams();
  body.append("username", username);
  body.append("password", password);

  const res = await fetch(`${BASE_URL}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: body.toString(),
  });

  if (!res.ok) {
    throw new Error("Login failed");
  }

  return res.json();
},


  register: async (username, password) => {
  const res = await fetch(`${BASE_URL}/auth/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, password }),
  });

  if (!res.ok) {
    throw new Error("Registration failed");
  }

  return res.json();
},


  recommend: (trackName, options = {}) => {
    const params = new URLSearchParams({
      track_name: trackName,
      ...options,
    }).toString();
    return request(`/recommend?${params}`);
  },

  playlists: () => request(`/playlists`),
};
recommendMulti: (trackNames, limit = 10) =>
  request(`/recommend/multi?limit=${limit}`, {
    method: "POST",
    body: JSON.stringify({
      track_names: trackNames,
    }),
  })