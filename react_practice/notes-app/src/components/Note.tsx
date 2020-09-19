import React from "react";
import DeleteIcon from "@material-ui/icons/Delete";

export type proptypes={
  key: number;
  id: number;
  title: string;
  content: string;
  noteselect: string;
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
      <p>{props.noteselect}</p>
      <button onClick={handlClick}>
        <DeleteIcon />
      </button>
    </div>
  );
}

export default Note;
