import React, { useState } from 'react';
import axios from 'axios';
import './LoginModal.css'; // Import modal-specific CSS

const LoginModal = ({ showModal, handleClose }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/login', { username, password });
      alert(response.data.message);
      if (response.status === 200) {
        handleClose(); // Close modal on successful login
      }
    } catch (error) {
      alert(error.response.data.message);
    }
  };

  const modalDisplayClass = showModal ? "modal display-block" : "modal";


  return (
    <div className={modalDisplayClass}>
      <div className="modal-main">
        <span className="close-button" onClick={handleClose}>×</span>
        <h2>Login</h2>
        <form onSubmit={handleLogin}>
          <label>Username</label>
          <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />
          <label>Password</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          <div className="modal-buttons">
            <button type="submit">Login</button>
            <button type="button" onClick={handleClose}>Cancel</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginModal;
