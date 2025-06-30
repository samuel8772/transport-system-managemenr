import React, { useEffect, useState } from 'react';

function Home() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    fetch('/api/test')
      .then((res) => res.json())
      .then((data) => setMessage(`✅ ${data.message}`))
      .catch(() => setMessage("❌ Backend not connected"));
  }, []);

  return (
    <div style={{ textAlign: 'center' }}>
      <h1>🚌 Matatu System</h1>
      <p>{message}</p>
    </div>
  );
}

export default Home;
