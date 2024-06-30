import React from 'react';
import './LoginModal.css'; // Ensure to have your CSS for the modal styles imported

const JoinModal = ({ showModal, handleClose, children }) => {
  if (!showModal) return null;

  return (
    <div className="modal display-block">
      <div className="modal-main">
        <span className="close-button" onClick={handleClose}>×</span>
        {children}
      </div>
    </div>
  );
};

export default JoinModal;