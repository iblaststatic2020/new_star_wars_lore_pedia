import React from 'react';
import { Link } from 'react-router-dom';

function Navbar({ toggleModal }) {
  return (
    <nav className="navbar">
      <h1>Custom Wikipedia</h1>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/create">Create Article</Link></li>
        <li><button onClick={toggleModal} className="login-button">Login</button></li>
        <li><Link to="/register">Sign Up</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
