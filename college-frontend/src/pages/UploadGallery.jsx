import React, { useState, useEffect } from 'react';
import { Button } from '../components/ui/button';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table';
import { Edit, Trash2 } from 'lucide-react';

const UploadGallery = () => {
  const [imageTitle, setImageTitle] = useState('');
  const [imageCategory, setImageCategory] = useState('');
  const [imageFile, setImageFile] = useState(null);
  const [galleryItems, setGalleryItems] = useState([]);

  const fetchGalleryItems = async () => {
    try {
      const response = await fetch('https://college-backend-api.onrender.com/api/gallery');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      setGalleryItems(data);
    } catch (error) {
      console.error("Error fetching gallery items:", error);
    }
  };

  useEffect(() => {
    fetchGalleryItems();
  }, []);

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
      const response = await fetch('https://college-backend-api.onrender.com/api/gallery', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`,
        },
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      alert('Image uploaded successfully!');
      setImageTitle('');
      setImageCategory('');
      setImageFile(null);
      fetchGalleryItems(); // Refresh the list after upload
    } catch (error) {
      console.error("Error uploading image:", error);
      alert('Error uploading image.');
    }
  };

  const handleEdit = (id) => {
    console.log('Edit gallery item:', id);
    // In a real application, you would navigate to an edit page or open a modal
  };

  const handleDelete = async (id) => {
    console.log('Delete gallery item:', id);
    try {
      const response = await fetch(`https://college-backend-api.onrender.com/api/gallery/${id}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`,
        },
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      fetchGalleryItems(); // Refresh the list after delete
    } catch (error) {
      console.error("Error deleting gallery item:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Manage Campus Gallery</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Upload New Image</h2>
          <form onSubmit={handleSubmit} className="space-y-4 mb-8">
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

          <h2 className="text-2xl font-bold text-gray-900 mb-4">Existing Gallery Items</h2>
          {galleryItems.length > 0 ? (
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Title</TableHead>
                  <TableHead>Category</TableHead>
                  <TableHead>Image</TableHead>
                  <TableHead className="text-right">Actions</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {galleryItems.map((item) => (
                  <TableRow key={item.id}>
                    <TableCell className="font-medium">{item.title}</TableCell>
                    <TableCell>{item.category}</TableCell>
                    <TableCell>
                      <img src={item.image_url} alt={item.title} className="h-16 w-16 object-cover rounded" />
                    </TableCell>
                    <TableCell className="text-right">
                      <Button variant="ghost" size="sm" onClick={() => handleEdit(item.id)} className="mr-2">
                        <Edit className="h-4 w-4" />
                      </Button>
                      <Button variant="destructive" size="sm" onClick={() => handleDelete(item.id)}>
                        <Trash2 className="h-4 w-4" />
                      </Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          ) : (
            <p className="text-gray-600">No gallery items uploaded yet.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default UploadGallery;
