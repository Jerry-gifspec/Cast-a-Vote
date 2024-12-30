// ScrollAnimations.jsx
import React, { useEffect } from "react";
import AOS from "aos";
import "aos/dist/aos.css";

const ScrollAnimations = ({ children }) => {
  useEffect(() => {
    AOS.init({ duration: 1000, offset: 200, easing: "ease-in-out" });
  }, []);

  return <div>{children}</div>;
};

export default ScrollAnimations;
