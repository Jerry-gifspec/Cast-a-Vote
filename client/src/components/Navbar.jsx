import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Navbar.css";

const Navbar = () => {
  const navigate = useNavigate();
  const [isDropdownOpen, setDropdownOpen] = useState(false);

  const handleLogout = () => {
    // Clear local storage and navigate to login
    localStorage.clear();
    navigate("/login");
  };

  const toggleDropdown = () => {
    setDropdownOpen(!isDropdownOpen);
  };

  return (
    <nav className="navbar">
      <div className="navbar-links">
        <Link to="/">Home</Link>
      </div>
      <div className="navbar-actions">
        {/* <button className="dropdown-button" onClick={toggleDropdown}>
          Menu
        </button> */}
        {isDropdownOpen && (
          <div className="dropdown-menu">
            <Link to="/about" className="dropdown-item">
              About Us
            </Link>
            <Link to="/contact" className="dropdown-item">
              Contact Us
            </Link>
            <Link to="/settings" className="dropdown-item">
              Settings
            </Link>
            <Link to="/login" className="dropdown-item">
              Login
            </Link>
          </div>
        )}
        <button onClick={handleLogout} className="logout-button">
          Logout
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
