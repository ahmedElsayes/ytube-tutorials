import React, { useState } from "react";
import Note from "./Note";
import CreateArea from "./CreateArea";

type NoteType = {
  key: number;
  id: number;
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

  const scores = [[10, 2], [4, 5], [0, 3]];
  const newScore = scores.map(function(subarray) {
    return subarray.map(function(number) {
      return number * 2;
    })
  })
  console.log(newScore);

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
