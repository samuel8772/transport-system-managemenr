import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // ✅ import navigate

function Login() {
  const [formData, setFormData] = useState({
    username: '',
    password: ''
  });
  const [message, setMessage] = useState('');
  const navigate = useNavigate(); // ✅ hook to redirect

  function handleChange(e) {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  }

  function handleSubmit(e) {
    e.preventDefault();
    fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include', // ✅ include cookies for session
      body: JSON.stringify(formData)
    })
      .then(res => res.json())
      .then(data => {
        if (data.error) {
          setMessage(`❌ ${data.error}`);
        } else {
          localStorage.setItem('token', data.access_token); // ✅ store token
          setMessage(`✅ Welcome back, ${data.username}!`);
          navigate('/trips'); // ✅ redirect after login
        }
      })
      .catch(() => setMessage('❌ Something went wrong. Try again.'));
  }

  return (
    <div>
      <h1>🔐 Login</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          required
        />
        <br />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />
        <br />
        <button type="submit">Login</button>
      </form>
      <p>{message}</p>
    </div>
  );
}

export default Login;
