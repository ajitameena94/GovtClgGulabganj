import React, { useState } from 'react';
import { Button } from '../components/ui/button';

const UploadGallery = () => {
  const [imageTitle, setImageTitle] = useState('');
  const [imageCategory, setImageCategory] = useState('');
  const [imageFile, setImageFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!imageFile) {
      alert('Please select an image file.');
      return;
    }

    const formData = new FormData();
    formData.append('title', imageTitle);
    formData.append('category', imageCategory);
    formData.append('file', imageFile);

    try {
      const response = await fetch('/api/gallery', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      alert('Image uploaded successfully!');
      setImageTitle('');
      setImageCategory('');
      setImageFile(null);
      // Optionally, redirect to ManageGallery or refresh a list
    } catch (error) {
      console.error("Error uploading image:", error);
      alert('Error uploading image.');
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Upload Gallery Image</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <form onSubmit={handleSubmit}>
            <div className="mb-4">
              <label htmlFor="imageTitle" className="block text-gray-700 font-bold mb-2">Image Title</label>
              <input type="text" id="imageTitle" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" value={imageTitle} onChange={(e) => setImageTitle(e.target.value)} required />
            </div>
            <div className="mb-4">
              <label htmlFor="imageCategory" className="block text-gray-700 font-bold mb-2">Image Category</label>
              <input type="text" id="imageCategory" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" value={imageCategory} onChange={(e) => setImageCategory(e.target.value)} required />
            </div>
            <div className="mb-4">
              <label htmlFor="imageFile" className="block text-gray-700 font-bold mb-2">Image File</label>
              <input type="file" id="imageFile" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" onChange={(e) => setImageFile(e.target.files[0])} required />
            </div>
            <Button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
              Upload Image
            </Button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default UploadGallery;
