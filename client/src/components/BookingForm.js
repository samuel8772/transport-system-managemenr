import React, { useEffect, useState } from 'react';

function BookingForm() {
  const [trips, setTrips] = useState([]);
  const [passengers, setPassengers] = useState([]);
  const [formData, setFormData] = useState({
    trip_id: '',
    passenger_id: '',
    seat_number: ''
  });
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('/api/trips/')
      .then((res) => res.json())
      .then(setTrips);

    fetch('/api/passengers/')
      .then((res) => res.json())
      .then(setPassengers);
  }, []);

  const handleChange = (e) => {
    setFormData((data) => ({
      ...data,
      [e.target.name]: e.target.value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/api/bookings/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.error) {
          setMessage(`❌ ${data.error}`);
        } else {
          setMessage('✅ Booking successful!');
          setFormData({ trip_id: '', passenger_id: '', seat_number: '' });
        }
      })
      .catch(() => setMessage('❌ Booking failed. Try again.'));
  };

  return (
    <div>
      <h2>📝 Book a Trip</h2>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <label>
          Trip:
          <select name="trip_id" value={formData.trip_id} onChange={handleChange} required>
            <option value="">-- Choose a trip --</option>
            {trips.map((trip) => (
              <option key={trip.id} value={trip.id}>
                #{trip.id} | {trip.route?.origin} → {trip.route?.destination} | 🪑 {trip.available_seats}
              </option>
            ))}
          </select>
        </label>
        <br />

        <label>
          Passenger:
          <select name="passenger_id" value={formData.passenger_id} onChange={handleChange} required>
            <option value="">-- Choose a passenger --</option>
            {passengers.map((p) => (
              <option key={p.id} value={p.id}>
                {p.name} ({p.phone_number})
              </option>
            ))}
          </select>
        </label>
        <br />

        <label>
          Seat Number:
          <input
            type="number"
            name="seat_number"
            value={formData.seat_number}
            onChange={handleChange}
            required
            min="1"
          />
        </label>
        <br />

        <button type="submit">🚍 Book Seat</button>
      </form>
    </div>
  );
}

export default BookingForm;
