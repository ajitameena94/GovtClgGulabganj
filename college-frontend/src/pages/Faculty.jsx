import React from 'react';

const Faculty = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Faculty</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Our Faculty</h2>
          <p className="text-lg text-gray-600 mb-6 leading-relaxed">
            Our experienced and dedicated faculty members are experts in their fields. 
            They are committed to providing our students with the best possible education.
          </p>
          {/* Add faculty profiles here */}
        </div>
      </div>
    </div>
  );
};

export default Faculty;
