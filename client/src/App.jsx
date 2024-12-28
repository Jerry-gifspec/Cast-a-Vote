import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
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
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/login" element={<Login />} />
        <Route path="/candidate-profile" element={<CandidateProfile />} />
        <Route path="/" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/dashboard" element={<VotingDashboard />} />
        <Route path="/results" element={<Results />} />
        <Route path="/admin" element={<AdminPanel />} />
        <Route path="/voter-register" element={<VoterRegister />} />
      </Routes>
    </Router>
  );
}

export default App;
