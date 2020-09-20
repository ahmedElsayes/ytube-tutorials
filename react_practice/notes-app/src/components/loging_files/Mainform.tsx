import React from "react";
import Form from "./Form";

// change this variable to switch between regestering and logging in
var userIsRegistered = true;

function Mainform() {
  return (
    <div className="container">
      {userIsRegistered ? <Form Bname="Login" /> : <Form Bname="register" />}
    </div>
  );
}

export default Mainform;
