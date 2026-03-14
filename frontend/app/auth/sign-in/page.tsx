"use client";

import React, { useState } from "react";
import { hash } from "crypto";

const SignIn = () => {
  // useState hook to capture the entered data by the user and pass to the backend API
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  // Helps clean the functions clean and organized by taking the process outside
  const ChangeEmail = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value);
    console.log(e.target.value);
  };
  const ChangePassword = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(e.target.value);
    console.log(e.target.value);
  };
  return (
    <div>
      <div>
        <div>Sign In</div>
        <input
          name="email"
          value={email}
          placeholder="Email"
          onChange={ChangeEmail}
          className="border-2 rounded-2xl "
        />
        <input
          name="password"
          value={password}
          onChange={ChangePassword}
          placeholder="Password"
          className="border-2 rounded-2xl "
          type="password"
        />
      </div>
      <div>Sign Out</div>
    </div>
  );
};

export default SignIn;
