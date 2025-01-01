import React from "react";
import "./HowToUse.css";

const HowToUse = () => {
  return (
    <div className="how-to-use">
      <h2>How to Use the App</h2>
      <div className="steps">
        <button type="button" className="step-button">
          <h3> Sign up</h3>
          <span className="arrow">→</span>
        </button>
        <button type="button" className="step-button">
          <h3> Log in</h3>
          <span className="arrow">→</span>
        </button>
        <button type="button" className="step-button">
          <h3> View elections</h3>
          <span className="arrow">→</span>
        </button>
        <button type="button" className="step-button">
          <h3> Cast vote</h3>
        </button>
      </div>
    </div>
  );
};

export default HowToUse;
