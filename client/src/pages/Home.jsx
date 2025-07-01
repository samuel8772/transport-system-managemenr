import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Home() {
  const [message, setMessage] = useState('Loading...');
  const navigate = useNavigate();

  useEffect(() => {
    fetch('/api/test')
      .then((res) => res.json())
      .then((data) => setMessage(`✅ ${data.message}`))
      .catch(() => setMessage("❌ Backend not connected"));
  }, []);

  const backgroundStyle = {
    backgroundImage: 'url("https://images.squarespace-cdn.com/content/v1/65a17d6335ed8079ddfc87f9/a8b516e9-a382-49d4-be02-43b6e92d82c3/basigo-e9-kubwa-hero-01.jpg")',
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    height: '100vh',
    color: 'white',
    textShadow: '1px 1px 3px black',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    padding: '20px'
  };

  const buttonStyle = {
    marginTop: '20px',
    padding: '12px 24px',
    fontSize: '1.1rem',
    backgroundColor: '#007bff',
    color: '#fff',
    border: 'none',
    borderRadius: '8px',
    cursor: 'pointer'
  };

  return (
    <div style={backgroundStyle}>
      <h1>🚌 Matatu System</h1>
      <p>{message}</p>
      <p>Book your matatu seat easily and quickly.</p>
      <button style={buttonStyle} onClick={() => navigate('/trips')}>
        Get Started
      </button>
    </div>
  );
}

export default Home;
