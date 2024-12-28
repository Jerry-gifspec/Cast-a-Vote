import React, { useState } from "react";
import axios from "axios";

const ManageCandidates = () => {
  const [formData, setFormData] = useState({
    name: "",
    description: "",
  });
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:5000/api/candidates",
        formData
      );
      setMessage(response.data.message);
    } catch (error) {
      setMessage("Error adding candidate");
    }
  };

  return (
    <div className="manage-candidates">
      <h2>Manage Candidates</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Name"
          onChange={handleChange}
          required
        />
        <textarea
          name="description"
          placeholder="Description"
          onChange={handleChange}
          required
        />
        <button type="submit">Add Candidate</button>
      </form>
      <p>{message}</p>
    </div>
  );
};

export default ManageCandidates;
