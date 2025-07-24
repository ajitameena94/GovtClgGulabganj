import React from 'react';

const ManageLibrary = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Manage Campus Library</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Upload New Resource</h2>
          <form className="space-y-4">
            <div>
              <label htmlFor="resourceTitle" className="block text-gray-700 font-bold mb-2">Resource Title</label>
              <input type="text" id="resourceTitle" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div>
              <label htmlFor="resourceFile" className="block text-gray-700 font-bold mb-2">Resource File</label>
              <input type="file" id="resourceFile" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
              Upload Resource
            </button>
          </form>

          <h2 className="text-2xl font-bold text-gray-900 mt-8 mb-4">Existing Resources</h2>
          {/* Placeholder for listing and deleting resources */}
          <p className="text-gray-600">List of uploaded library resources will appear here.</p>
        </div>
      </div>
    </div>
  );
};

export default ManageLibrary;
