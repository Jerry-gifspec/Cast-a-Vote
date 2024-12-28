import React from "react";

const Settings = () => {
  return (
    <div style={styles.container}>
      <h1 style={styles.header}>Settings</h1>
      <p style={styles.text}>
        Customize your preferences and manage your account settings here.
      </p>
      <ul style={styles.list}>
        <li>Update Profile</li>
        <li>Change Password</li>
        <li>Notification Preferences</li>
      </ul>
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
  list: {
    marginTop: "1rem",
    listStyleType: "none",
    padding: 0,
    fontSize: "1rem",
  },
};

export default Settings;
