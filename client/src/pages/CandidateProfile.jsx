import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const CandidateProfile = () => {
  const [candidateData, setCandidateData] = useState({
    name: "",
    age: "",
    city: "",
    contact: "",
    position: "",
    nationality: "",
    policy: "",
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    setCandidateData({ ...candidateData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:5000/api/candidate/register", // Corrected the URL
        candidateData
      );
      console.log("Candidate Registered:", response.data);
      navigate("/login");
    } catch (error) {
      console.error(
        "Error registering candidate:",
        error.response?.data || error.message
      );
    }
  };

  return (
    <div style={styles.container}>
      <h1>Candidate Profile</h1>
      <form onSubmit={handleSubmit} style={styles.form}>
        {Object.keys(candidateData).map((key) => (
          <input
            key={key}
            type={key === "age" ? "number" : "text"}
            name={key}
            placeholder={key.charAt(0).toUpperCase() + key.slice(1)}
            value={candidateData[key]}
            onChange={handleChange}
            required
          />
        ))}
        <button type="submit">Submit</button>
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

export default CandidateProfile;
