// src/pages/LoginPage.jsx
import React from 'react';
import Navbar from '../components/Navbar';

const LoginPage = () => {
  return (
    <div>
      <Navbar />

      <div style={{ maxWidth: '400px', margin: 'auto', marginTop: '3rem' }}>
        <h2 style={{ textAlign: 'center' }}>Giriş Yap</h2>

        <form style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          <input type="email" placeholder="E-posta" required />
          <input type="password" placeholder="Şifre" required />

          <button type="submit">Giriş Yap</button>

          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.9rem' }}>
            <button type="button" style={{ background: 'none', border: 'none', color: 'blue', cursor: 'pointer' }}>
              Şifremi Unuttum
            </button>
            <a href="/register">Kayıt Ol</a>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
