import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const VoterRegister = () => {
  const [voterData, setVoterData] = useState({
    name: "",
    city: "",
    contact: "",
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    setVoterData({ ...voterData, [e.target.name]: e.target.value });
  };

  const generateAadhar = () => {
    return Math.floor(100000000000 + Math.random() * 900000000000).toString();
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const aadhar = generateAadhar();
    try {
      const response = await axios.post(
        "http://localhost:5000/api/voter/register",
        {
          ...voterData,
          aadhar,
        }
      );
      console.log("Voter Registered:", response.data);
      navigate("/login");
    } catch (error) {
      console.error(
        "Error registering voter:",
        error.response?.data || error.message
      );
    }
  };

  return (
    <div style={styles.container}>
      <h1>Voter Registration</h1>
      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          type="text"
          name="name"
          placeholder="Name"
          value={voterData.name}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="city"
          placeholder="City"
          value={voterData.city}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="contact"
          placeholder="Contact"
          value={voterData.contact}
          onChange={handleChange}
          required
        />
        <button type="submit">Register</button>
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

export default VoterRegister;
