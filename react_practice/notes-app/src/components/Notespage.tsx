import React, { useState } from "react";
import Note from "./Note";
import CreateArea from "./CreateArea";

type NoteType = {
  title: string;
  content: string;
  noteselect: string;
};

function Notespage() {
 
  const [notes, setnotes] = useState([]);
  function addnote(newNote: NoteType) {
    setnotes((preNotes: NoteType[]): any => {
      return [...preNotes, newNote];
    });
  }

  function deletNote(id: number) {
    setnotes((prevNotes: NoteType[]): any => {
      return prevNotes.filter((noteItem: NoteType, index: number) => {
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
