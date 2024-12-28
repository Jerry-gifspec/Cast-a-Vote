import React from "react";

const Home = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.header}>Unlock Your Voting Power!</h1>
      <p style={styles.text}>Others:</p>
    </div>
  );
};

const styles = {
  container: {
    padding: "2rem",
    textAlign: "center",
  },
  header: {
    fontSize: "2.5rem",
    color: "#004080",
  },
  text: {
    fontSize: "1.2rem",
    color: "#333333",
  },
};

export default Home;
