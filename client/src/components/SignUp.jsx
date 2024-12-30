import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import ScrollAnimations from "../pages/ScrollAnimations";

const Signup = () => {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    role: "voter", // Default role
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Make API request to register user
      const response = await axios.post(
        "http://localhost:5000/api/signup",
        formData
      );

      alert(
        `Signup successful! ${
          formData.role === "voter"
            ? "Your Aadhar Number is generated. Please use it to log in."
            : ""
        }`
      );

      // Redirect based on role
      if (formData.role === "admin") {
        navigate("/admin-dashboard"); // Redirect to Admin Dashboard
      } else {
        navigate("/login"); // Redirect to Login Page for Voter
      }
    } catch (error) {
      console.error("Signup error:", error);
      alert("Failed to sign up. Please try again.");
    }
  };

  return (
    <div style={styles.container}>
      <ScrollAnimations>
        <h2 data-aos="fade-up">Sign Up</h2>
        <form onSubmit={handleSubmit} style={styles.form}>
          <input
            type="text"
            name="username"
            placeholder="Username"
            value={formData.username}
            onChange={handleChange}
            required
          />
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            required
          />
          <select name="role" value={formData.role} onChange={handleChange}>
            <option value="Voter">Voter</option>
            <option value="admin">Admin</option>
          </select>
          <button type="submit">Submit</button>
        </form>
      </ScrollAnimations>
    </div>
  );
};

const styles = {
  container: {
    textAlign: "center",
    padding: "2rem",
    color: "#4B3621",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "1rem",
    maxWidth: "300px",
    margin: "0 auto",
  },
};

export default Signup;
