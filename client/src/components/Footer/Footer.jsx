import React from "react";
import "./Footer.css";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <p>&copy; 2025 CAMASKO VOTER WAVE. @ All rights reserved.</p>
        <p>
          Empowering the Cameroonian community through fair and transparent
          elections.
        </p>
      </div>
      <div className="footer-links">
        <a href="/terms" className="footer-link">
          Terms of Service
        </a>
        <a href="/privacy" className="footer-link">
          Privacy Policy
        </a>
        <a href="/contact" className="footer-link">
          Contact Us
        </a>
      </div>
    </footer>
  );
};

export default Footer;
