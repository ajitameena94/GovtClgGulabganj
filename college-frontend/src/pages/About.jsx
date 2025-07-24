import React from 'react';

const About = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">About Us</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <p className="text-lg text-gray-600 mb-6 leading-relaxed">
            Government College of Gulabganj, Vidisha, established in 2015, is a premier 
            institution dedicated to providing quality higher education in the field of 
            Arts and Humanities. Located in the historic district of Vidisha, Madhya Pradesh, 
            our college has been serving the educational needs of the region with commitment and excellence.
          </p>
          <p className="text-lg text-gray-600 mb-8 leading-relaxed">
            We offer comprehensive Bachelor of Arts programs in six major disciplines, 
            fostering critical thinking, creativity, and academic excellence among our students. 
            Our experienced faculty and modern infrastructure create an ideal learning environment 
            for holistic development.
          </p>
        </div>
      </div>
    </div>
  );
};

export default About;
