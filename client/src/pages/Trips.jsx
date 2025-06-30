import React, { useEffect, useState, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';

function Trips() {
  const [trips, setTrips] = useState([]);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState('');
  const { user } = useContext(AuthContext);

  useEffect(() => {
    fetch('/api/trips', { credentials: 'include' })
      .then(res => res.ok ? res.json() : [])
      .then(data => {
        setTrips(data);
        setLoading(false);
      })
      .catch(() => {
        setTrips([]);
        setLoading(false);
      });
  }, []);

  function handleBooking(tripId) {
    const seat = prompt("Enter your preferred seat number:");

    if (!seat || isNaN(seat)) {
      return alert("❌ Please enter a valid seat number.");
    }

    fetch('/api/bookings', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify({
        trip_id: tripId,
        passenger_id: user?.id,
        seat_number: parseInt(seat)
      })
    })
      .then(res => res.json())
      .then(data => {
        if (data.error) {
          setMessage(`❌ ${data.error}`);
        } else {
          setMessage('✅ Booking successful!');
          setTrips(prev =>
            prev.map(t => t.id === tripId ? { ...t, available_seats: t.available_seats - 1 } : t)
          );
        }
      })
      .catch(() => setMessage('❌ Booking failed.'));
  }

  return (
    <div style={{ padding: '30px', fontFamily: 'Segoe UI, sans-serif' }}>
      <h2 style={{ textAlign: 'center', fontSize: '2rem', marginBottom: '20px' }}>🚌 Available Trips</h2>
      {message && (
        <div style={{
          textAlign: 'center',
          marginBottom: '20px',
          padding: '10px 20px',
          backgroundColor: message.includes('✅') ? '#d4edda' : '#f8d7da',
          color: message.includes('✅') ? '#155724' : '#721c24',
          border: message.includes('✅') ? '1px solid #c3e6cb' : '1px solid #f5c6cb',
          borderRadius: '8px',
          maxWidth: '500px',
          margin: '0 auto 20px auto'
        }}>
          {message}
        </div>
      )}
      {loading ? (
        <p style={{ textAlign: 'center' }}>Loading trips...</p>
      ) : trips.length === 0 ? (
        <p style={{ textAlign: 'center' }}>No trips available.</p>
      ) : (
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
          gap: '25px',
        }}>
          {trips.map(trip => (
            <div key={trip.id} style={{
              border: '1px solid #e0e0e0',
              borderRadius: '12px',
              padding: '20px',
              backgroundColor: '#ffffff',
              boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
              transition: 'transform 0.2s ease-in-out',
            }}>
              <h3 style={{ marginBottom: '10px', color: '#333' }}>
                {trip.route?.origin} → {trip.route?.destination}
              </h3>
              <p><strong>Date:</strong> {trip.date}</p>
              <p><strong>Time:</strong> {trip.departure_time}</p>
              <p><strong>Matatu:</strong> {trip.matatu?.plate_number}</p>
              <p><strong>Seats Left:</strong> {trip.available_seats}</p>
              <button
                onClick={() => handleBooking(trip.id)}
                style={{
                  marginTop: '10px',
                  padding: '10px 18px',
                  backgroundColor: '#007bff',
                  color: 'white',
                  fontWeight: 'bold',
                  border: 'none',
                  borderRadius: '6px',
                  cursor: 'pointer'
                }}
              >
                Book Now
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Trips;
