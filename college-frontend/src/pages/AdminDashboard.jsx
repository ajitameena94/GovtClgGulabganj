import React from 'react';
import { Button } from '../components/ui/button';
import { useAuth } from '../context/AuthContext';

const AdminDashboard = () => {
  const { admin, logout } = useAuth();

  return (
    <div className="min-h-screen bg-gray-100 py-20 px-4">
      <div className="container mx-auto">
        <div className="max-w-2xl mx-auto bg-white p-8 rounded-lg shadow-lg">
          <h1 className="text-3xl font-bold text-center mb-4">Admin Dashboard</h1>
          <p className="text-center text-gray-600 mb-6">
            Welcome, {admin?.username || 'Admin'}!
          </p>
          <div className="text-center">
            <Button onClick={logout} className="mr-4">
              Logout
            </Button>
            <Link to="/admin/upload-facilities">
              <Button>
                Go to Upload Facilities
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
