import React, { useEffect, useState } from "react";
import axios from "axios";
import "./ElectionPage.css"; // Optional: Add your styles here.

const ElectionPage = () => {
  const [elections, setElections] = useState([]); // Store elections
  const [loading, setLoading] = useState(true); // Manage loading state
  const [error, setError] = useState(null); // Handle errors

  // Fetch elections from the backend
  useEffect(() => {
    const fetchElections = async () => {
      try {
        const response = await axios.get("http://localhost:5000/api/elections");
        setElections(response.data.elections); // Update state with fetched data
        setLoading(false);
      } catch (err) {
        setError(err.response?.data?.message || "Failed to fetch elections");
        setLoading(false);
      }
    };

    fetchElections();
  }, []);

  if (loading) {
    return <div className="loading">Loading elections...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="election-container">
      <h1 className="election-title">Available Elections</h1>
      {elections.length === 0 ? (
        <p className="no-elections">No elections available at the moment.</p>
      ) : (
        <ul className="election-list">
          {elections.map((election) => (
            <li key={election.id} className="election-item">
              <h2>{election.name}</h2>
              <p>Date: {new Date(election.date).toLocaleDateString()}</p>
              <p>Description: {election.description}</p>
              <button
                onClick={() => handleElectionDetails(election.id)}
                className="details-btn">
                View Details
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

// Function to handle viewing election details
const handleElectionDetails = (electionId) => {
  // Redirect to a details page or show a modal (customize as needed)
  window.location.href = `/elections/${electionId}`;
};

export default ElectionPage;
