import React, { useState, useEffect } from 'react';
import { Button } from '../components/ui/button';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table';
import { Edit, Trash2 } from 'lucide-react';

const ManageGallery = () => {
  const [galleryItems, setGalleryItems] = useState([]);

  const fetchGalleryItems = async () => {
    try {
      const response = await fetch('/api/gallery');
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

  const handleEdit = (id) => {
    console.log('Edit gallery item:', id);
    // In a real application, you would navigate to an edit page or open a modal
  };

  const handleDelete = async (id) => {
    console.log('Delete gallery item:', id);
    try {
      const response = await fetch(`/api/gallery/${id}`, {
        method: 'DELETE',
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      fetchGalleryItems(); // Refresh the list
    } catch (error) {
      console.error("Error deleting gallery item:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Manage Campus Gallery</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
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

export default ManageGallery;
