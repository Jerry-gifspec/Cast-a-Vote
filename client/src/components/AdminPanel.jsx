import React from "react";
import { Link } from "react-router-dom";

const AdminDashboard = () => {
  return (
    <div style={styles.container}>
      <h1>Admin Dashboard</h1>
      <div style={styles.links}>
        <Link to="/register-voter" style={styles.button}>
          Register Voter
        </Link>
        <Link to="/register-candidate" style={styles.button}>
          Register Candidate
        </Link>
      </div>
    </div>
  );
};

const styles = {
  container: {
    textAlign: "center",
    padding: "2rem",
  },
  links: {
    display: "flex",
    justifyContent: "center",
    gap: "1rem",
    marginTop: "2rem",
  },
  button: {
    padding: "1rem 2rem",
    background: "#007bff",
    color: "#fff",
    textDecoration: "none",
    borderRadius: "5px",
    fontSize: "16px",
  },
};

export default AdminDashboard;
