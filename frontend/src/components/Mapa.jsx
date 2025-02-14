import React from 'react';
import { MapContainer, TileLayer, Marker } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

import { useParams } from 'react-router-dom';

const Mapa = () => {
  const { lat, lon } = useParams();

  const coordenadas = [parseFloat(lat), parseFloat(lon)];

  return (
    <div>
<MapContainer center={coordenadas} zoom={18} style={{ height: '100vh', width: '100vw' }}>
<TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors'
          url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
        />
        <Marker position={coordenadas} />
      </MapContainer>
    </div>
  );
};

export default Mapa;