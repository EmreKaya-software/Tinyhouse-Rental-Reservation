// src/components/Navbar.jsx
import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav style={{ background: '#eee', padding: '1rem' }}>
      <Link to="/" style={{ textDecoration: 'none', fontWeight: 'bold' }}>
        Anasayfa
      </Link>
    </nav>
  );
};

export default Navbar;
