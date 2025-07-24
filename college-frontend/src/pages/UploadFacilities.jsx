import React, { useState } from 'react';
import { Button } from '../components/ui/button';

const UploadFacilities = () => {
  const [facilityName, setFacilityName] = useState('');
  const [facilityDescription, setFacilityDescription] = useState('');
  const [facilityImage, setFacilityImage] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!facilityImage) {
      alert('Please select an image file.');
      return;
    }

    const formData = new FormData();
    formData.append('name', facilityName);
    formData.append('description', facilityDescription);
    formData.append('file', facilityImage);

    try {
      const response = await fetch('/api/facilities', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      alert('Facility uploaded successfully!');
      setFacilityName('');
      setFacilityDescription('');
      setFacilityImage(null);
    } catch (error) {
      console.error("Error uploading facility:", error);
      alert('Error uploading facility.');
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Upload Facilities</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <form onSubmit={handleSubmit}>
            <div className="mb-4">
              <label htmlFor="facilityName" className="block text-gray-700 font-bold mb-2">Facility Name</label>
              <input type="text" id="facilityName" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" value={facilityName} onChange={(e) => setFacilityName(e.target.value)} required />
            </div>
            <div className="mb-4">
              <label htmlFor="facilityDescription" className="block text-gray-700 font-bold mb-2">Facility Description</label>
              <textarea id="facilityDescription" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" value={facilityDescription} onChange={(e) => setFacilityDescription(e.target.value)} required></textarea>
            </div>
            <div className="mb-4">
              <label htmlFor="facilityImage" className="block text-gray-700 font-bold mb-2">Facility Image</label>
              <input type="file" id="facilityImage" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" onChange={(e) => setFacilityImage(e.target.files[0])} required />
            </div>
            <Button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
              Upload Facility
            </Button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default UploadFacilities;
