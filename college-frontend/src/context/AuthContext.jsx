import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export const useAuth = () => {
  return useContext(AuthContext);
};

export const AuthProvider = ({ children }) => {
  const [admin, setAdmin] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      // Optionally, validate the token with the backend here
      // For now, we'll just assume it's valid and set the admin state
      setAdmin({ username: 'admin' }); // You might want to store more admin info in the token
    }
    setLoading(false);
  }, []);

  const login = async (username, password, callback) => {
    try {
      const response = await fetch('https://college-backend-api.onrender.com/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();

      if (response.ok) {
        localStorage.setItem('token', data.access_token); // Store the token
        setAdmin(data.admin);
        setError(null);
        if (callback) callback();
      } else {
        setError(data.error || 'Login failed');
      }
    } catch (err) {
      setError('An unexpected error occurred. Please try again.');
      console.error('Login error:', err);
    }
  };

  const logout = () => {
    localStorage.removeItem('token'); // Remove the token
    setAdmin(null);
  };

  const value = {
    admin,
    loading,
    error,
    login,
    logout,
  };

  return <AuthContext.Provider value={value}>{!loading && children}</AuthContext.Provider>;
};
