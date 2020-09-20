import React, { useState } from "react";
import Note from "./Note";
import CreateArea from "./CreateArea";

function Notespage() {
  const [notes, setnotes] = useState([]);
  function addnote(newNote: any) {
    setnotes((preNotes: any): any => {
      return [...preNotes, newNote];
    });
  }

  function deletNote(id: number) {
    setnotes((prevNotes: any): any => {
      return prevNotes.filter((noteItem: any, index: number) => {
        return index !== id;
      });
    });
  }

  return (
    <div>
      <CreateArea onadd={addnote} />
      {notes.map((noteItem: any, index: number) => {
        return (
          <Note
            key={index}
            id={index}
            title={noteItem.title}
            content={noteItem.content}
            noteselect={noteItem.noteselect}
            del={deletNote}
          />
        );
      })}
    </div>
  );
}

export default Notespage;
