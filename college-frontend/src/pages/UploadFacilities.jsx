import React from 'react';

const UploadFacilities = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Upload Facilities</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <form>
            <div className="mb-4">
              <label htmlFor="facilityName" className="block text-gray-700 font-bold mb-2">Facility Name</label>
              <input type="text" id="facilityName" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div className="mb-4">
              <label htmlFor="facilityDescription" className="block text-gray-700 font-bold mb-2">Facility Description</label>
              <textarea id="facilityDescription" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"></textarea>
            </div>
            <div className="mb-4">
              <label htmlFor="facilityImage" className="block text-gray-700 font-bold mb-2">Facility Image</label>
              <input type="file" id="facilityImage" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
              Upload Facility
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default UploadFacilities;