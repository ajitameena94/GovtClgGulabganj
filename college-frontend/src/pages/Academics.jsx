import React from 'react';

const Academics = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Academics</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">BA Programs</h2>
          <p className="text-lg text-gray-600 mb-6 leading-relaxed">
            We offer a variety of Bachelor of Arts programs to suit your academic interests. 
            Our programs are designed to provide a strong foundation in the liberal arts and prepare you for a successful career.
          </p>
          <ul className="list-disc list-inside text-lg text-gray-600">
            <li>BA History</li>
            <li>BA Economics</li>
            <li>BA Sociology</li>
            <li>BA Political Science</li>
            <li>BA Hindi Literature</li>
            <li>BA English Literature</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Academics;
