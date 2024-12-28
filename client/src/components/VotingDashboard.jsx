import React, { useEffect, useState } from "react";
import axios from "axios";

const VotingDashboard = () => {
  const [candidates, setCandidates] = useState([]);
  const [message, setMessage] = useState("");

  useEffect(() => {
    const fetchCandidates = async () => {
      try {
        const response = await axios.get(
          "http://localhost:5000/api/candidates"
        );
        setCandidates(response.data);
      } catch (error) {
        setMessage("Error fetching candidates");
      }
    };
    fetchCandidates();
  }, []);

  const handleVote = async (candidateId) => {
    try {
      const token = localStorage.getItem("token");
      const response = await axios.post(
        `http://localhost:5000/api/vote/${candidateId}`,
        {},
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setMessage(response.data.message);
    } catch (error) {
      setMessage("Error submitting vote");
    }
  };

  return (
    <div className="voting-dashboard">
      <h2>Voting Dashboard</h2>
      {candidates.map((candidate) => (
        <div key={candidate.candidate_id}>
          <h3>{candidate.name}</h3>
          <p>{candidate.description}</p>
          <button onClick={() => handleVote(candidate.candidate_id)}>
            Vote
          </button>
        </div>
      ))}
      <p>{message}</p>
    </div>
  );
};

export default VotingDashboard;
