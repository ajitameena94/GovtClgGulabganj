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
    const checkAuth = async () => {
      const token = localStorage.getItem('token');
      if (token) {
        try {
          const response = await fetch('https://college-backend-api.onrender.com/api/auth/check-auth', {
            headers: {
              'Authorization': `Bearer ${token}`,
            },
          });
          const data = await response.json();
          if (response.ok && data.authenticated) {
            setAdmin(data.admin);
          } else {
            localStorage.removeItem('token'); // Clear invalid token
            setAdmin(null);
          }
        } catch (err) {
          console.error('Error checking auth status:', err);
          localStorage.removeItem('token');
          setAdmin(null);
        } finally {
          setLoading(false);
        }
      } else {
        setLoading(false);
      }
    };

    checkAuth();
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
