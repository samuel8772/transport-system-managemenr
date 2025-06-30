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

    fetch('/api/bookings', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        trip_id: selectedTrip.id,
        seat_number: seatNumber
      })
    })
      .then(res => res.json())
      .then(data => {
        if (data.error) {
          setMessage(`❌ ${data.error}`);
        } else {
          setMessage('✅ Seat booked successfully!');
          setSeatNumber('');
          setSelectedTrip(null);
        }
      })
      .catch(() => setMessage('❌ Booking failed'));
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
