import React, {useState} from "react";
import DeleteIcon from "@material-ui/icons/Delete";
import RemoveIcon from "@material-ui/icons/Remove";
import Modal from "react-modal";
Modal.setAppElement("#root");

const customStyles = {
  overlay: {
    backgroundColor: "rgba(255, 255, 255, 0.75)"
  },
  content : {
    top: '50%',
    left: '50%',
    right: 'auto',
    bottom: 'auto',
    marginRight: '-50%',
    transform: 'translate(-50%, -50%)'
  }
};
 

type proptypes={
  key: number;
  id: number;
  title: string;
  content: string;
  noteselect: string;
  del: (id: number) => void;
}
function Note(props: proptypes) {
  function handlClick() {
    props.del(props.id);
  }
  const [modalTrigger, setModalTrigger] = useState(false);

  return (
    <div>
      <div
        className="note"
        onClick={() => {
          setModalTrigger(true);
        }}
      >
        <h1>{props.title}</h1>
        <p>{props.content}</p>
        <p>{props.noteselect}</p>
        <button onClick={handlClick}>
          <DeleteIcon />
        </button>
      </div>
      <Modal
        isOpen={modalTrigger}
        style={customStyles}
        onRequestClose={() => {
          setModalTrigger(false);
        }}
      >
        <h1>This is example to test Modal working</h1>
        <p>{props.title}</p>
        <p>{props.content}</p>
        <p>{props.noteselect}</p>
        <button
          onClick={() => {
            setModalTrigger(false);
          }}
        >
          <RemoveIcon />
        </button>
      </Modal>
    </div>
  );
}

export default Note;
