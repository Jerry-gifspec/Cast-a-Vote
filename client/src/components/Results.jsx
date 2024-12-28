import React, { useEffect, useState } from "react";
import axios from "axios";

const Results = () => {
  const [results, setResults] = useState([]);

  useEffect(() => {
    const fetchResults = async () => {
      try {
        const response = await axios.get("http://localhost:5000/api/results");
        setResults(response.data);
      } catch (error) {
        console.error("Error fetching results");
      }
    };
    fetchResults();
  }, []);

  return (
    <div className="results">
      <h2>Results</h2>
      {results.map((candidate) => (
        <div key={candidate.candidate_id}>
          <h3>{candidate.name}</h3>
          <p>Votes: {candidate.votes}</p>
        </div>
      ))}
    </div>
  );
};

export default Results;
