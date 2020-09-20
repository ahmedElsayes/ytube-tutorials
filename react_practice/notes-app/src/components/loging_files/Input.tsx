import React from "react";

interface typeprops {
  type: string;
  placeholder: string;
}

function Input(props: typeprops) {
  return <input type={props.type} placeholder={props.placeholder} />;
}

export default Input;
