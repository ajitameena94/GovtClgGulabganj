import React from 'react';

const Admissions = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Admissions</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Admission Process</h2>
          <p className="text-lg text-gray-600 mb-6 leading-relaxed">
            The admission process for the academic year 2024-25 is now open. 
            Please visit the official website for more information on the admission process, eligibility criteria, and important dates.
          </p>
          <a href="#" className="text-lg text-blue-500 hover:underline">Official Admission Portal</a>
        </div>
      </div>
    </div>
  );
};

export default Admissions;
