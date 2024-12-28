import React, { useState } from "react";
import axios from "axios";

const Login = () => {
  const [loginData, setLoginData] = useState({
    usernameOrAadhar: "",
    password: "",
  });

  const handleChange = (e) => {
    setLoginData({ ...loginData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:5000/api/login",
        loginData
      );
      localStorage.setItem("token", response.data.token);
      alert("Login successful");
    } catch (error) {
      console.error(
        "Error during login:",
        error.response?.data || error.message
      );
      alert("Login failed");
    }
  };

  return (
    <div style={styles.container}>
      <h1>Login</h1>
      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          type="text"
          name="usernameOrAadhar"
          placeholder="Username or Aadhar Number"
          value={loginData.usernameOrAadhar}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={loginData.password}
          onChange={handleChange}
          required
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

const styles = {
  container: {
    textAlign: "center",
    padding: "2rem",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "1rem",
    maxWidth: "300px",
    margin: "0 auto",
  },
};

export default Login;
