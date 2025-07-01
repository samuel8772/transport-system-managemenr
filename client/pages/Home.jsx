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

  return (
    <div
      style={{
        backgroundImage: "url('https://imgcdn.oto.com.sg/medium/gallery/exterior/1/7/toyota-hiace-commuter-16838.jpg')",
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        minHeight: '100vh',
        paddingTop: '100px',
        textAlign: 'center',
        color: '#fff',
      }}
    >
      <h1 style={{ fontSize: '3rem', fontWeight: 'bold' }}>🚌 Matatu System</h1>
      <p style={{ fontSize: '1.5rem' }}>{message}</p>
      <button
        style={{
          marginTop: '2rem',
          padding: '1rem 2rem',
          fontSize: '1.2rem',
          backgroundColor: '#007bff',
          color: '#fff',
          border: 'none',
          borderRadius: '8px',
          cursor: 'pointer',
        }}
        onClick={() => navigate('/trips')}
      >
        Get Started
      </button>
    </div>
  );
}

export default Home;
