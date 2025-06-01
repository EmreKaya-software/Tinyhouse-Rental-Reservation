// src/pages/HousesPage.jsx
import React, { useEffect, useState } from 'react';

const HousesPage = () => {
  const [houses, setHouses] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/get_all_houses')
      .then((res) => res.json())
      .then((data) => setHouses(data))
      .catch((err) => console.error('Evler getirilemedi:', err));
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Tüm Evler</h1>
      {houses.length === 0 ? (
        <p>Yükleniyor...</p>
      ) : (
        <ul>
          {houses.map((house) => (
            <li key={house.house_id} style={{ marginBottom: '1rem' }}>
              <h3>{house.title}</h3>
              <p><strong>Konum:</strong> {house.location}</p>
              <p><strong>Fiyat:</strong> {house.price_per_night} TL / gece</p>
              <p><strong>Açıklama:</strong> {house.description}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default HousesPage;
