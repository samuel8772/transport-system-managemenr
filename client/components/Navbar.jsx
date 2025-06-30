import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav style={{ padding: '10px', backgroundColor: '#333', color: 'white' }}>
      <Link to="/" style={{ marginRight: '15px', color: 'white' }}>Home</Link>
      <Link to="/login" style={{ marginRight: '15px', color: 'white' }}>Login</Link>
      <Link to="/register" style={{ color: 'white' }}>Register</Link>
    </nav>
  );
}

export default Navbar;
