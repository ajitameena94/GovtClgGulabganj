import React, { useState } from 'react';
import { Button } from '../components/ui/button';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Textarea } from '../components/ui/textarea';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../components/ui/select';
import { useAuth } from '../context/AuthContext';

const UploadGallery = () => {
  const { admin } = useAuth();
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [category, setCategory] = useState('events');
  const [eventDate, setEventDate] = useState('');
  const [image, setImage] = useState(null);
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const categories = [
    { value: 'events', label: 'Events' },
    { value: 'infrastructure', label: 'Infrastructure' },
    { value: 'activities', label: 'Activities' },
    { value: 'faculty', label: 'Faculty' },
    { value: 'students', label: 'Students' },
    { value: 'achievements', label: 'Achievements' },
    { value: 'campus', label: 'Campus Life' },
  ];

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage('');
    setError('');

    if (!image) {
      setError('Please select an image to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('title', title);
    formData.append('description', description);
    formData.append('category', category);
    formData.append('event_date', eventDate);
    formData.append('image', image);

    try {
      const response = await fetch('http://localhost:5001/api/gallery/upload', {
        method: 'POST',
        body: formData,
        // No Content-Type header needed for FormData, browser sets it automatically
      });

      const data = await response.json();

      if (response.ok) {
        setMessage(data.message);
        // Clear form
        setTitle('');
        setDescription('');
        setCategory('events');
        setEventDate('');
        setImage(null);
        document.getElementById('image-upload').value = '';
      } else {
        setError(data.error || 'Failed to upload image.');
      }
    } catch (err) {
      setError('An unexpected error occurred. Please try again.');
      console.error('Upload error:', err);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 py-20 px-4">
      <div className="container mx-auto">
        <Card className="max-w-2xl mx-auto">
          <CardHeader>
            <CardTitle className="text-2xl font-bold text-center">Upload Gallery Image</CardTitle>
            <p className="text-center text-gray-600">Add a new image to the college gallery.</p>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="space-y-2">
                <Label htmlFor="title">Title</Label>
                <Input
                  id="title"
                  type="text"
                  placeholder="Enter image title"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  required
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="description">Description</Label>
                <Textarea
                  id="description"
                  placeholder="Enter image description (optional)"
                  value={description}
                  onChange={(e) => setDescription(e.target.value)}
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="category">Category</Label>
                <Select value={category} onValueChange={setCategory}>
                  <SelectTrigger className="w-full">
                    <SelectValue placeholder="Select a category" />
                  </SelectTrigger>
                  <SelectContent>
                    {categories.map((cat) => (
                      <SelectItem key={cat.value} value={cat.value}>
                        {cat.label}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              <div className="space-y-2">
                <Label htmlFor="eventDate">Event Date (Optional)</Label>
                <Input
                  id="eventDate"
                  type="date"
                  value={eventDate}
                  onChange={(e) => setEventDate(e.target.value)}
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="image-upload">Image File</Label>
                <Input
                  id="image-upload"
                  type="file"
                  accept="image/*"
                  onChange={(e) => setImage(e.target.files[0])}
                  required
                />
              </div>

              {message && <p className="text-green-600 text-center">{message}</p>}
              {error && <p className="text-red-600 text-center">{error}</p>}

              <Button type="submit" className="w-full">
                Upload Image
              </Button>
            </form>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default UploadGallery;
