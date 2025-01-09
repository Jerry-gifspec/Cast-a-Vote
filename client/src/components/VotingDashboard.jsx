import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom"; // For accessing URL parameters
import axios from "axios";

const VotingDashboard = () => {
  const { electionId } = useParams(); // Get the electionId from the URL
  const [candidates, setCandidates] = useState([]);
  const [message, setMessage] = useState("");

  useEffect(() => {
    const fetchCandidates = async () => {
      try {
        const response = await axios.get(
          `http://localhost:5000/api/elections/${electionId}/candidates`
        );
        setCandidates(response.data);
      } catch (error) {
        setMessage("Error fetching candidates");
      }
    };
    fetchCandidates();
  }, [electionId]);

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
      <h2>Voting Dashboard for Election {electionId}</h2>
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
