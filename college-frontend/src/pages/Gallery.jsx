import React, { useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';

const Gallery = () => {
  const [galleryItems, setGalleryItems] = useState([]);

  useEffect(() => {
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

    fetchGalleryItems();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Campus Gallery</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Explore Our Campus</h2>
          {galleryItems.length > 0 ? (
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
              {galleryItems.map((item) => (
                <Card key={item.id} className="overflow-hidden">
                  <img 
                    src={item.image_url} 
                    alt={item.title}
                    className="w-full h-48 object-cover"
                  />
                  <CardContent className="p-4">
                    <CardTitle className="text-lg">{item.title}</CardTitle>
                    <p className="text-sm text-gray-600">{item.category}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
          ) : (
            <p className="text-gray-600">No gallery items available at the moment.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Gallery;
