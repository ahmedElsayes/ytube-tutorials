import React from "react";

export type proptypes={
  key: number;
  id: number;
  title: string;
  content: string;
  del: Function;
}
function Note(props: proptypes) {
  function handlClick() {
    props.del(props.id);
  }

  return (
    <div className="note">
      <h1>{props.title}</h1>
      <p>{props.content}</p>
      <button onClick={handlClick}>DELETE</button>
    </div>
  );
}

export default Note;
