import React, { useEffect } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import AOS from "aos";
import "aos/dist/aos.css";
import Login from "./pages/Login";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import About from "./pages/About";
import Contact from "./pages/Contact";
import VoterRegister from "./pages/VoterRegister";
import CandidateProfile from "./pages/CandidateProfile";
import Signup from "./components/SignUp";
import VotingDashboard from "./components/VotingDashboard";
import Results from "./components/Results";
import AdminPanel from "./components/AdminPanel";

function App() {
  // Initialize AOS
  useEffect(() => {
    AOS.init({
      duration: 1200, // Animation duration in milliseconds
      offset: 100, // Offset before animation starts
      easing: "ease-in-out", // Animation easing
      once: true, // Whether animation should happen only once
    });
  }, []);

  return (
    <Router>
      <Navbar />
      <Routes>
        <Route
          path="/"
          element={
            <>
              <div data-aos="fade-up">
                <Home />
              </div>
              <div data-aos="fade-left">
                <Signup />
              </div>
              <div data-aos="fade-right">
                <About />
              </div>
            </>
          }
        />
        <Route
          path="/about"
          element={
            <div data-aos="zoom-in">
              <About />
            </div>
          }
        />
        <Route
          path="/contact"
          element={
            <div data-aos="fade-up">
              <Contact />
            </div>
          }
        />
        <Route
          path="/login"
          element={
            <div data-aos="flip-left">
              <Login />
            </div>
          }
        />
        <Route
          path="/candidate-profile"
          element={
            <div data-aos="fade-up">
              <CandidateProfile />
            </div>
          }
        />
        <Route
          path="/dashboard"
          element={
            <div data-aos="fade-right">
              <VotingDashboard />
            </div>
          }
        />
        <Route
          path="/results"
          element={
            <div data-aos="zoom-out">
              <Results />
            </div>
          }
        />
        <Route
          path="/admin"
          element={
            <div data-aos="fade-left">
              <AdminPanel />
            </div>
          }
        />
        <Route
          path="/voter-register"
          element={
            <div data-aos="fade-up">
              <VoterRegister />
            </div>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
