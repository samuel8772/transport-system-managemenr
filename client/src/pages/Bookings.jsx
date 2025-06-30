// src/pages/Bookings.jsx
import React, { useEffect, useState } from 'react';

function Bookings() {
  const [bookings, setBookings] = useState([]);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('/api/bookings', { credentials: 'include' })
      .then(res => res.ok ? res.json() : [])
      .then(data => {
        setBookings(data);
        setLoading(false);
      })
      .catch(() => {
        setBookings([]);
        setLoading(false);
        setMessage('❌ Failed to load bookings.');
      });
  }, []);

  function handleCancel(id) {
    if (!window.confirm("Are you sure you want to cancel this booking?")) return;

    fetch(`/api/bookings/${id}`, {
      method: 'DELETE',
      credentials: 'include'
    })
      .then(res => res.ok ? res.json() : Promise.reject())
      .then(() => {
        setBookings(prev => prev.filter(b => b.id !== id));
        setMessage('✅ Booking cancelled.');
      })
      .catch(() => {
        setMessage('❌ Failed to cancel booking.');
      });
  }

  return (
    <div style={{ padding: '20px' }}>
      <h2>📋 My Bookings</h2>
      {message && <p>{message}</p>}

      {loading ? (
        <p>Loading bookings...</p>
      ) : bookings.length === 0 ? (
        <p>You have no bookings yet.</p>
      ) : (
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
          gap: '20px'
        }}>
          {bookings.map(booking => {
            const trip = booking.trip;
            const route = trip?.route;
            const matatu = trip?.matatu;

            return (
              <div key={booking.id} style={{
                border: '1px solid #ccc',
                borderRadius: '10px',
                padding: '15px',
                backgroundColor: '#fff',
                boxShadow: '0 4px 8px rgba(0,0,0,0.1)'
              }}>
                <h3>🛣 {route?.origin} → {route?.destination}</h3>
                <p><strong>Date:</strong> {trip?.date}</p>
                <p><strong>Time:</strong> {trip?.departure_time}</p>
                <p><strong>Matatu:</strong> {matatu?.plate_number}</p>
                <p><strong>Your Seat:</strong> {booking.seat_number}</p>
                <button
                  onClick={() => handleCancel(booking.id)}
                  style={{
                    marginTop: '10px',
                    backgroundColor: '#e53935',
                    color: 'white',
                    border: 'none',
                    padding: '8px 12px',
                    cursor: 'pointer',
                    borderRadius: '6px'
                  }}
                >
                  ❌ Cancel Booking
                </button>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default Bookings;
