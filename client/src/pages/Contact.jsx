import React from "react";

const Contact = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.header}>Contact Us</h1>
      <p style={styles.text}>
        We would love to hear from you! Reach out to us via email at{" "}
        <a href="mailto:support@mywebsite.com">support@mywebsite.com</a>
        or call us at <strong>+123 456 7890</strong>.
      </p>
      <p style={styles.text}>
        You can also connect with us on our social media channels for more
        updates and support.
      </p>
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

export default Contact;
