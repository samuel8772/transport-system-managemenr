// src/pages/Bookings.js
import React, { useEffect, useState } from 'react';

function Bookings() {
  const [bookings, setBookings] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/bookings') // ✅ This assumes your Flask route is setup like this
      .then((res) => {
        if (!res.ok) throw new Error("Network response was not ok");
        return res.json();
      })
      .then((data) => {
        setBookings(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching bookings:", error);
        setBookings([]);
        setLoading(false);
      });
  }, []);

  return (
    <div>
      <h2>🧾 My Bookings</h2>
      {loading ? (
        <p>⏳ Loading your bookings...</p>
      ) : bookings.length === 0 ? (
        <p>No bookings found.</p>
      ) : (
        <ul>
          {bookings.map((booking) => (
            <li key={booking.id}>
              🚐 Trip ID: {booking.trip_id} | Seat No: {booking.seat_number}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Bookings;
