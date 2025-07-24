import React from 'react';

const Contact = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Contact Us</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Get in Touch</h2>
          <p className="text-lg text-gray-600 mb-6 leading-relaxed">
            We are here to help you with any questions you may have. Please feel free to contact us using the information below.
          </p>
          <div className="flex flex-col md:flex-row md:space-x-8">
            <div className="flex-1">
              <h3 className="text-xl font-bold text-gray-900 mb-2">Address</h3>
              <p className="text-lg text-gray-600">Government College, Gulabganj, Vidisha, Madhya Pradesh, 464220</p>
            </div>
            <div className="flex-1">
              <h3 className="text-xl font-bold text-gray-900 mb-2">Email</h3>
              <p className="text-lg text-gray-600">info@govtcollegegulabganj.ac.in</p>
            </div>
            <div className="flex-1">
              <h3 className="text-xl font-bold text-gray-900 mb-2">Phone</h3>
              <p className="text-lg text-gray-600">+91 123 456 7890</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact;
