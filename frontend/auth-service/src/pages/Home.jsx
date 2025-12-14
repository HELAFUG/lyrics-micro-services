import React from "react";
import { Link } from "react-router-dom";

const Home = () => (
  <div className="min-h-screen bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center p-4">
    <div className="text-center text-white">
      <h1 className="text-5xl font-bold mb-8">Auth Service Frontend</h1>
      <div className="space-x-4">
        <Link to="/login" className="bg-white text-indigo-600 py-3 px-8 rounded-lg font-semibold hover:bg-gray-100">Login</Link>
        <Link to="/register" className="bg-white text-indigo-600 py-3 px-8 rounded-lg font-semibold hover:bg-gray-100">Register</Link>
      </div>
    </div>
  </div>
);

export default Home;