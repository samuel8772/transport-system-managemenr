import React, { useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

function Navbar() {
  const { user, setUser } = useContext(AuthContext);
  const navigate = useNavigate();

  function handleLogout() {
    fetch('/api/auth/logout', {
      method: 'POST',
      credentials: 'include'
    })
      .then(() => {
        setUser(null);
        navigate('/');
      })
      .catch(() => alert('Logout failed'));
  }

  return (
    <nav style={{ padding: '10px', backgroundColor: '#333', color: 'white' }}>
      <Link to="/" style={{ marginRight: '15px', color: 'white' }}>Home</Link>

      {user ? (
        <>
          <Link to="/bookings" style={{ marginRight: '15px', color: 'white' }}>Bookings</Link>
          <Link to="/trips" style={{ marginRight: '15px', color: 'white' }}>Trips</Link>
          
          {user.role === 'admin' && (
            <Link to="/admin" style={{ marginRight: '15px', color: 'white' }}>Admin</Link>
          )}

          <button
            onClick={handleLogout}
            style={{
              color: 'white',
              background: 'transparent',
              border: 'none',
              cursor: 'pointer'
            }}
          >
            Logout
          </button>
        </>
      ) : (
        <>
          <Link to="/login" style={{ marginRight: '15px', color: 'white' }}>Login</Link>
          <Link to="/register" style={{ color: 'white' }}>Register</Link>
        </>
      )}
    </nav>
  );
}

export default Navbar;
