import React from 'react';

const Notifications = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Notifications</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Latest Notifications</h2>
          <p className="text-lg text-gray-600 mb-6 leading-relaxed">
            Stay up-to-date with the latest news and announcements from the college.
          </p>
          {/* Add notifications here */}
        </div>
      </div>
    </div>
  );
};

export default Notifications;
