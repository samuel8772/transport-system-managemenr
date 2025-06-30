import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <h2>🚌 Matatu System</h2>
      <div className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/login">Login</Link>
        <Link to="/register">Register</Link>
        <Link to="/bookings">Bookings</Link>
        <Link to="/trips">Trips</Link> {/* ✅ Add this */}
      </div>
    </nav>
  );
}

export default Navbar;
