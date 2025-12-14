import React from "react";
import { useAuth } from "../context/AuthContext";
import { Link } from "react-router-dom";

const Dashboard = () => {
  const { user, logout } = useAuth();

  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md p-8 text-center">
        <h2 className="text-3xl font-bold text-gray-800 mb-4">Dashboard</h2>
        <p className="text-gray-600 mb-8">Welcome! You are logged in.</p>
        <p className="text-sm break-all mb-8">Token: {user?.token}</p>
        <button onClick={logout} className="bg-red-600 text-white py-3 px-6 rounded-lg hover:bg-red-700">
          Logout
        </button>
        <p className="mt-6"><Link to="/" className="text-indigo-600 hover:underline">Back to Home</Link></p>
      </div>
    </div>
  );
};

export default Dashboard;