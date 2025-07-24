import React from 'react';

const ManageTimetables = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Manage Timetables</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Upload New Timetable</h2>
          <form className="space-y-4">
            <div>
              <label htmlFor="timetableTitle" className="block text-gray-700 font-bold mb-2">Timetable Title</label>
              <input type="text" id="timetableTitle" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div>
              <label htmlFor="timetableFile" className="block text-gray-700 font-bold mb-2">Timetable File (PDF/Image)</label>
              <input type="file" id="timetableFile" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
              Upload Timetable
            </button>
          </form>

          <h2 className="text-2xl font-bold text-gray-900 mt-8 mb-4">Existing Timetables</h2>
          {/* Placeholder for listing and deleting timetables */}
          <p className="text-gray-600">List of uploaded timetables will appear here.</p>
        </div>
      </div>
    </div>
  );
};

export default ManageTimetables;
