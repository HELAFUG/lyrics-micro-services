import axios from "axios";

const API_BASE = "http://localhost:8040/api/v1/auth";

export const api = axios.create({
    baseURL: API_BASE,
});

const login = (data) => api.post("/login", data);
const register = (data) => api.post("/register", data);


export default api;