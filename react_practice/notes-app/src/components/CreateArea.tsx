import React, { useState } from "react";

interface proptype {
  onadd: Function;
}

function CreateArea(props: proptype) {
  const [note, setNote] = useState({
    title: "",
    content: ""
  });

  function handleChange(event:any) {
    const { name, value } = event.target;

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
        <button onClick={buttonpress}>Add</button>
      </form>
    </div>
  );
}

export default CreateArea;
