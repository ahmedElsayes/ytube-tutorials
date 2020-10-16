import React, { useState } from "react";
import AddIcon from "@material-ui/icons/Add";
import Select from "@material-ui/core/Select";
import MenuItem from "@material-ui/core/MenuItem";
import InputLabel from "@material-ui/core/InputLabel";
import classNames from "classnames";
// npm install @types/react-router-dom    # to install react routes in typescript project
// npm install @material-ui/core          # to install material-ui in typescript project

type proptype = {
  onadd: Function;
}

export default function CreateArea({onadd}: proptype) {
  const [note, setNote] = useState({
    title: "",
    content: "",
    noteselect: "",
  });

  function handleChange(event: any) {
    const { name, value } = event.target;
    console.log(value);
    setNote((prevNote) => {
      return {
        ...prevNote,
        [name]: value,
      };
    });
  }

  // function handleChange1(event: any) {
  //   const { name, value } = event.target;
  //   // console.log(value);
  //   setNote((prevNote) => {
  //     console.log(prevNote);
  //     return {
  //       ...prevNote,
  //       title: value,
  //     };
  //   });
  // }
  const [pressed, setPressed] = useState(false);
  function buttonpress(event:any) {
    setPressed(!pressed);
    onadd(note);
    setNote({
      title: "",
      content: "",
      noteselect: "",
    });
    event.preventDefault();
  }
  const [textSpace, setTextSpace] = useState(false);
  function expandText(){
    setTextSpace(true);
  }

  return (
    <div className="notes-editor">
      <form>
        {textSpace ? (
          <input
            name="title"
            value={note.title}
            placeholder="Title"
            onChange={handleChange}
          />
        ) : null}

        <textarea
          value={note.content}
          onClick={expandText}
          name="content"
          placeholder="Take a note..."
          onChange={handleChange}
          rows={textSpace ? 5 : 2}
        />

        {/* <select
          name="noteselect"
          value={note.noteselect}
          onChange={handleChange}
        >
          <option value="">Make selection</option>
          <option value="Personal notes">Personal note</option>
          <option value="Work notes">Work note</option>
          <option value="Notes for planned projects">
            Another purpose note
          </option>
        </select> */}
        <InputLabel id="demo-simple-select-label">Note type</InputLabel>
        <Select
          className="dropdownMenu"
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          name="noteselect"
          value={note.noteselect}
          onChange={handleChange}
        >
          <MenuItem value="Personal notes">Personal note</MenuItem>
          <MenuItem value="Work notes">Work note</MenuItem>
          <MenuItem value="Notes for planned projects">
            Another purposes
          </MenuItem>
        </Select>
        <button className={classNames("note_button--idle", {"note_button--active": pressed})} onClick={buttonpress}>
          <AddIcon />
        </button>
      </form>
    </div>
  );
}
