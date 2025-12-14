import React from "react";
import AuthForm from "../components/AuthForm";
import { Link } from "react-router-dom";

const RegisterPage = () => (
  <div className="min-h-screen bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center p-4">
    <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md p-8">
      <h2 className="text-3xl font-bold text-center text-gray-800 mb-8">Create Account</h2>
      <AuthForm isRegister />
      <p className="text-center mt-6 text-gray-600">
        Already have an account? <Link to="/login" className="text-indigo-600 font-semibold hover:underline">Login</Link>
      </p>
    </div>
  </div>
);

export default RegisterPage;