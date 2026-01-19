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
  login: (username, password) =>
    request(`/auth/login?username=${username}&password=${password}`, {
      method: "POST",
    }),

  register: (username, password) =>
    request(`/auth/register?username=${username}&password=${password}`, {
      method: "POST",
    }),

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
  }),
