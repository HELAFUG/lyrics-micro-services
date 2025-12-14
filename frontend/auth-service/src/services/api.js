import axios from "axios";

const API_BASE = "http://localhost:8040/api/v1/auth";

const api = axios.create({
  baseURL: API_BASE,
});

export const register = (data) => api.post("/register", data);
export const login = (data) => api.post("/login", data);

export default api;