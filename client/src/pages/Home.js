import React from 'react';
import { useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate();

  const containerStyle = {
    position: 'relative',
    height: '100vh',
    overflow: 'hidden',
  };

  const backgroundStyle = {
    backgroundImage: 'url("https://imgcdn.oto.com.sg/medium/gallery/exterior/1/7/toyota-hiace-commuter-16838.jpg")',
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    height: '100%',
    width: '100%',
    position: 'absolute',
    top: 0,
    left: 0,
    zIndex: 0,
  };

  const overlayStyle = {
    position: 'absolute',
    top: 0,
    left: 0,
    height: '100%',
    width: '100%',
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    zIndex: 1,
  };

  const contentStyle = {
    position: 'relative',
    zIndex: 2,
    height: '100%',
    color: 'white',
    textShadow: '1px 1px 3px black',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    padding: '20px',
    textAlign: 'center',
  };

  const buttonStyle = {
    marginTop: '20px',
    padding: '12px 24px',
    fontSize: '1rem',
    backgroundColor: '#28a745',
    color: 'white',
    border: 'none',
    borderRadius: '8px',
    cursor: 'pointer',
    boxShadow: '2px 2px 8px rgba(0,0,0,0.4)',
    transition: 'transform 0.2s, background-color 0.3s',
  };

  const handleMouseOver = (e) => {
    e.target.style.transform = 'scale(1.05)';
    e.target.style.backgroundColor = '#218838';
  };

  const handleMouseOut = (e) => {
    e.target.style.transform = 'scale(1)';
    e.target.style.backgroundColor = '#28a745';
  };

  const handleClick = () => {
    navigate('/register');
  };

  return (
    <div style={containerStyle}>
      <div style={backgroundStyle} />
      <div style={overlayStyle} />
      <div style={contentStyle}>
        <h1>🚌 Welcome to Matatu System</h1>
        <p>Book your matatu seat easily and quickly.</p>
        <button
          onClick={handleClick}
          onMouseOver={handleMouseOver}
          onMouseOut={handleMouseOut}
          style={buttonStyle}
        >
          Get Started
        </button>
      </div>
    </div>
  );
}

export default Home;
