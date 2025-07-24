import React from 'react';

const UploadGallery = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Upload Gallery</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <form>
            <div className="mb-4">
              <label htmlFor="imageTitle" className="block text-gray-700 font-bold mb-2">Image Title</label>
              <input type="text" id="imageTitle" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div className="mb-4">
              <label htmlFor="imageCategory" className="block text-gray-700 font-bold mb-2">Image Category</label>
              <input type="text" id="imageCategory" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div className="mb-4">
              <label htmlFor="imageFile" className="block text-gray-700 font-bold mb-2">Image File</label>
              <input type="file" id="imageFile" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
              Upload Image
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default UploadGallery;