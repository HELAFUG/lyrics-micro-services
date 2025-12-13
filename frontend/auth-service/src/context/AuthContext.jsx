import React, { createContext, useContext, useState, useEffect } from "react";
import { login as loginApi, register as registerApi } from "../services/api";
import toast from "react-hot-toast";

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      // You could decode/validate token here (e.g., check expiry with jwt-decode)
      setUser({ token });
    }
    setLoading(false);
  }, []);

  const login = async (credentials) => {
    try {
      const res = await loginApi(credentials);
      const token = res.data.token || res.data.accessToken;
      if (!token) throw new Error("No token received");
      localStorage.setItem("token", token);
      setUser({ token });
      toast.success("Login successful!");
      return true;
    } catch (err) {
      toast.error(err.response?.data?.message || "Login failed");
      return false;
    }
  };

  const register = async (credentials) => {
    try {
      await registerApi(credentials);
      toast.success("Registration successful! Please log in.");
      return true;
    } catch (err) {
      toast.error(err.response?.data?.message || "Registration failed");
      return false;
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    setUser(null);
    toast.success("Logged out");
  };

  return (
    <AuthContext.Provider value={{ user, login, register, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};