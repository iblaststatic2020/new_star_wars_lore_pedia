import React, { useState } from 'react';
import JoinModal from './JoinModal'; // Import your Modal component here
import './Footer.css'

const Footer = () => {
    const [showModal, setShowModal] = useState(false);
    const [email, setEmail] = useState('');
  
    const toggleModal = () => {
      setShowModal(!showModal);
    };
  
    const handleEmailSubmit = () => {
      // Implement email submission logic here
      console.log(email); // Placeholder for handling email submission
      setShowModal(false); // Close modal after submission
    };
  
    return (
      <footer className="footer">
        <div className="ask-to-join">
          <button className="ask-button" onClick={toggleModal}>Ask to join!</button>
          <JoinModal showModal={showModal} handleClose={toggleModal}>
            <h2>Ask to join!</h2>
            <form onSubmit={handleEmailSubmit}>
              <label>Email</label>
              <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
              <div className="modal-buttons">
                <button type="submit">Submit</button>
                <button type="button" onClick={toggleModal}>Cancel</button>
              </div>
            </form>
          </JoinModal>
        </div>
      </footer>
    );
  };
  
  export default Footer;
