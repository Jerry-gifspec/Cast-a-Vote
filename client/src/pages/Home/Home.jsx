import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import ScrollAnimations from "./ScrollAnimations"; // Import your ScrollAnimations component
import "./Home.css";

const Home = () => {
  const [isDropdownOpen, setDropdownOpen] = useState(false);
  const [displayText, setDisplayText] = useState("");
  const phrase = "Unlock Your Voting Power!";

  const toggleDropdown = () => {
    setDropdownOpen(!isDropdownOpen);
  };

  useEffect(() => {
    let index = 0;
    const intervalId = setInterval(() => {
      if (index < phrase.length) {
        setDisplayText((prev) => prev + phrase[index]);
        index++;
      } else {
        clearInterval(intervalId); // Stop the interval when the full phrase is displayed
      }
    }, 100); // Typing speed (in ms)

    return () => clearInterval(intervalId); // Cleanup interval on unmount
  }, []);

  return (
    <div>
      <ScrollAnimations>
        <div style={styles.container}>
          <h1 style={styles.header} data-aos="fade-down">
            Unlock Your Voting Power!
          </h1>
          <p style={styles.text} data-aos="fade-up">
            Your participation matters.
          </p>
        </div>
      </ScrollAnimations>
    </div>
  );
};

const styles = {
  container: {
    padding: "2rem",
    textAlign: "center",
    display: "flex",
    flexDirection: "column",
    gap: "10px",
    alignItems: "center",
  },
  header: {
    fontSize: "2.5rem",
    color: "#4B3621",
  },
  text: {
    fontSize: "1.2rem",
    color: "#333333",
  },
  // Other styles...
};

export default Home;
