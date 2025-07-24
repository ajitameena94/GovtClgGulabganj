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
      try {
        const response = await fetch('http://localhost:5001/api/auth/check-auth', {
          credentials: 'include'
        });
        const data = await response.json();
        if (data.authenticated) {
          setAdmin(data.admin);
        }
      } catch (err) {
        console.error('Error checking auth status:', err);
      }
      setLoading(false);
    };

    checkAuth();
  }, []);

  const login = async (username, password) => {
    try {
      const response = await fetch('https://college-backend-api.onrender.com/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
        credentials: 'include'
      });

      const data = await response.json();

      if (response.ok) {
          setAdmin(data.admin);
          setError(null);
          window.location.href = '/GovtClgGulabganj/admin/upload-facilities'; // Redirect on success
        } else {
        setError(data.error || 'Login failed');
      }
    } catch (err) {
      setError('An unexpected error occurred. Please try again.');
      console.error('Login error:', err);
    }
  };

  const logout = async () => {
    try {
      await fetch('YOUR_RENDER_BACKEND_URL/api/auth/logout', { method: 'POST', credentials: 'include' });
      setAdmin(null);
    } catch (err) {
      console.error('Logout error:', err);
    }
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
