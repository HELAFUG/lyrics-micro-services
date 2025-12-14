import React from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

const schema = z.object({
  email: z.string().email("Invalid email").refine((val) => val.endsWith("@some_email_service.com"), {
    message: "Email must be from @some_email_service.com",
  }),
  password: z.string().min(6, "Password must be at least 6 characters"),
});

const AuthForm = ({ isRegister = false }) => {
  const { login, register } = useAuth();
  const navigate = useNavigate();
  const {
    register: reg,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm({ resolver: zodResolver(schema) });

  const onSubmit = async (data) => {
    const success = isRegister ? await register(data) : await login(data);
    if (success && !isRegister) {
      navigate("/dashboard");
    } else if (success && isRegister) {
      navigate("/login");
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">Email</label>
        <input
          {...reg("email")}
          type="email"
          className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          placeholder="user@some_email_service.com"
        />
        {errors.email && <p className="text-red-600 text-sm mt-1">{errors.email.message}</p>}
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">Password</label>
        <input
          {...reg("password")}
          type="password"
          className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          placeholder="••••••••"
        />
        {errors.password && <p className="text-red-600 text-sm mt-1">{errors.password.message}</p>}
      </div>

      <button
        type="submit"
        disabled={isSubmitting}
        className="w-full bg-indigo-600 text-white py-3 rounded-lg font-semibold hover:bg-indigo-700 transition disabled:opacity-50"
      >
        {isSubmitting ? "Processing..." : isRegister ? "Register" : "Login"}
      </button>
    </form>
  );
};

export default AuthForm;