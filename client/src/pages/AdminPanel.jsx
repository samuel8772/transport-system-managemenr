import React, { useContext } from 'react';
import { AuthContext } from '../context/AuthContext';

function AdminPanel() {
  const { user } = useContext(AuthContext);

  if (!user || user.role !== 'admin') {
    return <p>⛔ Access denied. Admins only.</p>;
  }

  return (
    <div style={{ padding: '20px' }}>
      <h2>🛠️ Admin Panel</h2>
      <ul>
        <li><a href="/admin/routes">Manage Routes</a></li>
        <li><a href="/admin/matatus">Manage Matatus</a></li>
        <li><a href="/admin/trips">Manage Trips</a></li>
      </ul>
    </div>
  );
}

export default AdminPanel;
