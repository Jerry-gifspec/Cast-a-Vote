import React from "react";

const About = () => {
  return (
    <div style={styles.container}>
      <h2 style={styles.header}>About Us</h2>
      <ul style={styles.list}>
        <div>
          <h3>We seek to:</h3>
        </div>
        <li>
          Unite Cameroonians in South Korea through democratic engagement.
        </li>
        <li>
          Empower our community to shape its future with fairness and
          inclusivity.
        </li>
        <li>
          Connecting Cameroonians in South Korea with a shared vision for
          progress and unity.
        </li>
        <li>
          Foster transparency, accountability, and active participation in our
          electoral process.
        </li>
        <li>
          Strengthening our community ties through innovative and secure voting
          practices.
        </li>
      </ul>
      <div style={styles.scheduleContainer}>
        <h2 style={styles.brand}>Schedule </h2>
        <a
          href="/Calendar.pdf"
          target="_blank"
          rel="noopener noreferrer"
          style={styles.link}>
          <button type="submit">View Calendar</button>
        </a>
      </div>
    </div>
  );
};

const styles = {
  container: {
    padding: "2rem",
    textAlign: "center",
    maxWidth: "600px", // Narrower width for the content
    margin: "0 auto", // Center the content on the page
  },
  header: {
    fontSize: "2.5rem",
    color: "#4B3621", // Dark coffee color
  },
  list: {
    textAlign: "left", // Aligns the list items to the left
    margin: "1rem 0",
    padding: "0 1rem",
    fontSize: "1.2rem",
    color: "#333333",
  },
  text: {
    fontSize: "1.2rem",
    color: "#333333",
  },
  scheduleContainer: {
    marginTop: "1rem", // Adds spacing between the list and "Schedule"
  },
  link: {
    fontSize: "1.2rem",
    color: "#007BFF", // Blue link color
    textDecoration: "none",
  },
};

export default About;
