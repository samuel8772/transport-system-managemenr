// src/pages/Trips.js
import React, { useEffect, useState } from 'react';

function Trips() {
  const [trips, setTrips] = useState([]);
  const [selectedTrip, setSelectedTrip] = useState(null);
  const [seatNumber, setSeatNumber] = useState('');
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('/api/trips')
      .then(res => res.json())
      .then(data => setTrips(data))
      .catch(() => setMessage('❌ Failed to load trips'));
  }, []);

  const handleBook = () => {
    if (!selectedTrip || !seatNumber) {
      setMessage('⚠️ Please select a trip and enter a seat number');
      return;
    }

    const token = localStorage.getItem('token');

    fetch('/api/bookings', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({
        trip_id: selectedTrip.id,
        seat_number: seatNumber
      })
    })
      .then(async res => {
        const data = await res.json();
        if (!res.ok) {
          setMessage(`❌ ${data.error || data.message || 'Unknown error occurred'}`);
        } else {
          setMessage('✅ Seat booked successfully!');
          setSeatNumber('');
          setSelectedTrip(null);
        }
      })
      .catch((err) => {
        console.error("Booking error:", err);
        setMessage('❌ Booking failed (server not responding)');
      });
  };

  return (
    <div>
      <h2>🛣️ Available Trips</h2>
      {message && <p>{message}</p>}

      <ul>
        {trips.map(trip => (
          <li key={trip.id}>
            <strong>Route:</strong> {trip.route?.origin} → {trip.route?.destination} <br />
            <strong>Matatu:</strong> {trip.matatu?.registration_number} <br />
            <strong>Departure:</strong> {new Date(trip.departure_time).toLocaleString()} <br />
            <strong>Seats:</strong> {trip.available_seats}
            <br />
            <button onClick={() => setSelectedTrip(trip)}>
              Select this Trip
            </button>
            <hr />
          </li>
        ))}
      </ul>

      {selectedTrip && (
        <div style={{ marginTop: '20px' }}>
          <h3>🪑 Book Seat for Trip #{selectedTrip.id}</h3>
          <input
            type="number"
            placeholder="Enter seat number"
            value={seatNumber}
            onChange={e => setSeatNumber(e.target.value)}
          />
          <button onClick={handleBook}>Confirm Booking</button>
        </div>
      )}
    </div>
  );
}

export default Trips;
