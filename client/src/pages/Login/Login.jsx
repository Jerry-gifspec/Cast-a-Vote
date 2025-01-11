import React, { useState } from "react";
import axios from "axios";
import "./Login.css"; // Ensure the CSS file exists for styling.

const Login = () => {
  // Initialize loginData state with fields: username and aadhar
  const [loginData, setLoginData] = useState({
    username: "", // Username field
    aadhar: "", // Aadhar number field
  });

  // Handle input field changes
  const handleChange = (e) => {
    setLoginData({ ...loginData, [e.target.name]: e.target.value });
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Ensure either username or aadhar is provided
      if (!loginData.username && !loginData.aadhar) {
        alert("Please enter your username or Aadhar number.");
        return;
      }

      // Prepare loginData to send
      const loginDataToSend = {
        username: loginData.username || "",
        aadhar: loginData.aadhar || "",
      };

      // Send the login request
      const response = await axios.post(
        "http://localhost:5000/api/auth/voter/login",
        loginDataToSend
      );

      console.log(response.data);

      // Store token and redirect to elections page
      localStorage.setItem("token", response.data.token);
      window.location.href = "/elections";
    } catch (error) {
      console.error(
        "Error during login:",
        error.response?.data || error.message
      );
      alert(error.response?.data?.message || "Login failed");
    }
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h1 className="login-title">Login</h1>
        <form onSubmit={handleSubmit} className="login-form">
          {/* Username Input */}
          <div className="form-group">
            <label>Username</label>
            <input
              type="text"
              name="username"
              placeholder="Enter your username"
              value={loginData.username}
              onChange={handleChange}
              className="form-input"
            />
          </div>
          {/* Aadhar Input */}
          <div className="form-group">
            <label>Aadhar Number</label>
            <input
              type="text"
              name="aadhar"
              placeholder="Enter your Aadhar number"
              value={loginData.aadhar}
              onChange={handleChange}
              className="form-input"
            />
          </div>

          {/* Submit Button */}
          <button type="submit" className="submit-btn">
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
