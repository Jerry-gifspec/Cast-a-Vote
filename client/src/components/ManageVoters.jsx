import React, { useState } from "react";
import axios from "axios";

const ManageVoters = () => {
  const [formData, setFormData] = useState({
    name: "",
    aadhar: "",
    password: "",
  });
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:5000/api/voters",
        formData
      );
      setMessage(response.data.message);
    } catch (error) {
      setMessage("Error adding voter");
    }
  };

  return (
    <div className="manage-voters">
      <h2>Manage Voters</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Name"
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="aadhar"
          placeholder="Aadhar Number"
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleChange}
          required
        />
        <button type="submit">Add Voter</button>
      </form>
      <p>{message}</p>
    </div>
  );
};

export default ManageVoters;
