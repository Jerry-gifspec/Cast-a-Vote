// import React, { useState } from "react";
// import axios from "axios";

// const Login = () => {
//   const [loginData, setLoginData] = useState({
//     email: "", // Changed from usernameOrAadhar since your DB uses email
//     password: "",
//     userType: "voter", // Added to distinguish between voters and admins
//   });

//   const handleChange = (e) => {
//     setLoginData({ ...loginData, [e.target.name]: e.target.value });
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       // Updated endpoint to match your backend structure
//       const endpoint =
//         loginData.userType === "admin"
//           ? "/api/auth/admin/login"
//           : "/api/auth/voter/login";

//       const response = await axios.post(
//         `http://localhost:5000${endpoint}`,
//         loginData
//       );

//       // Store additional user info along with token
//       localStorage.setItem("token", response.data.token);
//       localStorage.setItem("userType", loginData.userType);

//       // Redirect based on user type
//       if (loginData.userType === "admin") {
//         // Redirect to admin dashboard
//         window.location.href = "/admin/dashboard";
//       } else {
//         // Redirect to voter dashboard
//         window.location.href = "/voter/dashboard";
//       }
//     } catch (error) {
//       console.error(
//         "Error during login:",
//         error.response?.data || error.message
//       );
//       alert(error.response?.data?.message || "Login failed");
//     }
//   };

//   return (
//     <div className="min-h-screen flex items-center justify-center bg-gray-50">
//       <div className="max-w-md w-full space-y-8 p-8 bg-white rounded-lg shadow">
//         <h1 className="text-2xl font-bold text-center">Login</h1>
//         <form onSubmit={handleSubmit} className="space-y-6">
//           <div>
//             <select
//               name="userType"
//               value={loginData.userType}
//               onChange={handleChange}
//               className="w-full p-2 border rounded">
//               <option value="voter">Voter</option>
//               <option value="admin">Admin</option>
//             </select>
//           </div>

//           <div>
//             <input
//               type="email"
//               name="email"
//               placeholder="Email Address"
//               value={loginData.email}
//               onChange={handleChange}
//               required
//               className="w-full p-2 border rounded"
//             />
//           </div>

//           <div>
//             <input
//               type="password"
//               name="password"
//               placeholder="Password"
//               value={loginData.password}
//               onChange={handleChange}
//               required
//               className="w-full p-2 border rounded"
//             />
//           </div>

//           <button
//             type="submit"
//             className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600">
//             Login
//           </button>
//         </form>
//       </div>
//     </div>
//   );
// };

// export default Login;

import React, { useState } from "react";
import axios from "axios";
import "./Login.css"; // Make sure this file is created for styling.

const Login = () => {
  const [loginData, setLoginData] = useState({
    name: "",
    aadhar: "",
    userType: "voter", // Voter or Admin
  });

  const handleChange = (e) => {
    setLoginData({ ...loginData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const endpoint =
        loginData.userType === "admin"
          ? "/api/auth/admin/login"
          : "/api/auth/voter/login";

      const response = await axios.post(
        `http://localhost:5000${endpoint}`,
        loginData
      );

      localStorage.setItem("token", response.data.token);
      localStorage.setItem("userType", loginData.userType);

      window.location.href =
        loginData.userType === "admin"
          ? "/admin/dashboard"
          : "/voter/dashboard";
    } catch (error) {
      console.error(
        "Error during login:",
        error.response?.data || error.message
      );
      alert(error.response?.data?.message || "Login failed");
    }
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h1 className="login-title">Login</h1>
        <form onSubmit={handleSubmit} className="login-form">
          {/* User Type Selector */}
          <div className="form-group">
            <label>User Type</label>
            <select
              name="userType"
              value={loginData.userType}
              onChange={handleChange}
              className="form-input">
              <option value="voter">Voter</option>
              <option value="admin">Admin</option>
            </select>
          </div>

          {/* Name Input */}
          <div className="form-group">
            <label>Name</label>
            <input
              type="text"
              name="name"
              placeholder="Enter your name"
              value={loginData.name}
              onChange={handleChange}
              required
              className="form-input"
            />
          </div>

          {/* Aadhar Input */}
          <div className="form-group">
            <label>Aadhar Number</label>
            <input
              type="text"
              name="aadhar"
              placeholder="Enter your Aadhar number"
              value={loginData.aadhar}
              onChange={handleChange}
              required
              className="form-input"
            />
          </div>

          {/* Submit Button */}
          <button type="submit" className="submit-btn">
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
