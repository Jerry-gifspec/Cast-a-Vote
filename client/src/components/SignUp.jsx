import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import ScrollAnimations from "../pages/ScrollAnimations";

const Signup = () => {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    role: "voter",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const navigate = useNavigate();

  const validateForm = () => {
    if (!formData.username.trim()) {
      setError("Username is required");
      return false;
    }
    if (!formData.email.trim()) {
      setError("Email is required");
      return false;
    }
    if (!/\S+@\S+\.\S+/.test(formData.email)) {
      setError("Please enter a valid email address");
      return false;
    }
    if (formData.password.length < 6) {
      setError("Password must be at least 6 characters long");
      return false;
    }
    return true;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({ ...prevData, [name]: value }));
    setError(null); // Clear error when user makes changes
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    if (!validateForm()) {
      return;
    }

    setLoading(true);

    try {
      const response = await axios.post(
        "http://localhost:5000/api/signup",
        formData,
        {
          headers: {
            "Content-Type": "application/json",
          },
          timeout: 5000, // 5 second timeout
        }
      );

      const { message, aadhar_number } = response.data;

      // Store any necessary data in localStorage
      if (aadhar_number) {
        localStorage.setItem("aadhar_number", aadhar_number);
      }

      // Success message based on role
      const successMessage =
        formData.role === "voter"
          ? `Signup successful! Your Aadhar Number is: ${aadhar_number}`
          : "Admin account created successfully!";

      alert(successMessage);

      // Redirect based on role
      navigate(formData.role === "admin" ? "/admin-dashboard" : "/login");
    } catch (error) {
      console.error("Signup error:", error);

      // Handle different types of errors
      if (error.response) {
        // Server responded with error
        switch (error.response.status) {
          case 400:
            setError(error.response.data.message || "Invalid input data");
            break;
          case 409:
            setError("User already exists with this email");
            break;
          case 500:
            setError("Server error. Please try again later");
            break;
          default:
            setError("Failed to sign up. Please try again");
        }
      } else if (error.request) {
        // No response received
        setError("No response from server. Please check your connection");
      } else {
        setError("Failed to send request");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <ScrollAnimations>
        <h2 data-aos="fade-up">Sign Up</h2>
        <form onSubmit={handleSubmit} style={styles.form}>
          {error && <div style={styles.error}>{error}</div>}

          <input
            type="text"
            name="username"
            placeholder="Username"
            value={formData.username}
            onChange={handleChange}
            autoComplete="username"
            disabled={loading}
            style={styles.input}
            required
          />

          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            autoComplete="email"
            disabled={loading}
            style={styles.input}
            required
          />

          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            autoComplete="new-password"
            disabled={loading}
            style={styles.input}
            required
          />

          <select
            name="role"
            value={formData.role}
            onChange={handleChange}
            disabled={loading}
            style={styles.select}>
            <option value="voter">Voter</option>
            <option value="admin">Admin</option>
          </select>

          <button type="submit" disabled={loading} style={styles.button}>
            {loading ? "Signing up..." : "Submit"}
          </button>
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
  error: {
    backgroundColor: "#ffebee",
    color: "#c62828",
    padding: "0.75rem",
    borderRadius: "4px",
    marginBottom: "1rem",
  },
  input: {
    padding: "0.75rem",
    borderRadius: "4px",
    border: "1px solid #ccc",
    fontSize: "1rem",
  },
  select: {
    padding: "0.75rem",
    borderRadius: "4px",
    border: "1px solid #ccc",
    fontSize: "1rem",
  },
  button: {
    padding: "0.75rem",
    borderRadius: "4px",
    border: "none",
    backgroundColor: "#4B3621",
    color: "white",
    fontSize: "1rem",
    cursor: "pointer",
    ":disabled": {
      opacity: 0.7,
      cursor: "not-allowed",
    },
  },
};

export default Signup;
