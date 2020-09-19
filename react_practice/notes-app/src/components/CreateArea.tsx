import React, { useState } from "react";
import AddIcon from "@material-ui/icons/Add";
import Select from "@material-ui/core/Select";
import MenuItem from "@material-ui/core/MenuItem";
import InputLabel from "@material-ui/core/InputLabel";

interface proptype {
  onadd: Function;
}

function CreateArea(props: proptype) {
  const [note, setNote] = useState({
    title: "",
    content: "",
    noteselect: ""
  });

  function handleChange(event:any) {
    const { name, value } = event.target;
    console.log(value);
    setNote((prevNote) => {
      return {
        ...prevNote,
        [name]: value,
      };
    });
  }

  function buttonpress(event:any) {
    props.onadd(note);
    setNote({
      title: "",
      content: "",
      noteselect: ""
    });
    event.preventDefault();
  }

  return (
    <div>
      <form>
        <input
          name="title"
          value={note.title}
          placeholder="Title"
          onChange={handleChange}
        />
        <textarea
          value={note.content}
          name="content"
          placeholder="Take a note..."
          onChange={handleChange}
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
        <button onClick={buttonpress}>
          <AddIcon />
        </button>
      </form>
    </div>
  );
}

export default CreateArea;
