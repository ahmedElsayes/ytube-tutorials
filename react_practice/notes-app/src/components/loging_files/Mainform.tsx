import React, {useState} from "react";
import Form from "./Form";
import MenuItem from "@material-ui/core/MenuItem";
import InputLabel from "@material-ui/core/InputLabel";
import Select from "@material-ui/core/Select";

// change this variable to switch between regestering and logging in
// var userIsRegistered = true;

function Mainform() {

  const [userState, setUserState] = useState(false);
  const [userName, setUserName] = useState("");
  function handleChange(event: any) {
    const userstatus = event.target.value;
    userstatus === "login" ? setUserState(true) : setUserState(false);
    setUserName(userstatus);
  }

  return (
    <div>
      <div className="dropdownMenu_loginPage">
        <InputLabel id="demo-simple-select-label">Note type</InputLabel>
        <Select
          className="dropdownMenu"
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          name="formName"
          value={userName}
          onChange={handleChange}
        >
          <MenuItem value="login">Login</MenuItem>
          <MenuItem value="register">Register</MenuItem>
        </Select>
      </div>
      <div className="containerC">
        {userState ? <Form Bname="Login" /> : <Form Bname="register" />}
      </div>
    </div>
  );
}

export default Mainform;
