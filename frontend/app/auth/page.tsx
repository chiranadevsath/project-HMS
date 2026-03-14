import React from "react";
import Link from "next/link";

const Auth = () => {
  return (
    <div>
      <Link className="bg-blue-100 rounded-2xl w-full " href="/auth/sign-in">
        Sign In / Sign Up
      </Link>
    </div>
  );
};

export default Auth;
