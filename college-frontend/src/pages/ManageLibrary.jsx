import React, { useState } from 'react';
import { Button } from '../components/ui/button';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table';
import { Edit, Trash2 } from 'lucide-react';

const ManageLibrary = () => {
  const [resources, setResources] = useState([
    { id: 1, title: 'Introduction to Algorithms', file: 'algorithms.pdf' },
    { id: 2, title: 'Calculus for Engineers', file: 'calculus.pdf' },
    { id: 3, title: 'History of India', file: 'india_history.pdf' },
  ]);

  const handleEdit = (id) => {
    console.log('Edit resource:', id);
    // In a real application, you would navigate to an edit page or open a modal
  };

  const handleDelete = (id) => {
    console.log('Delete resource:', id);
    setResources(resources.filter(resource => resource.id !== id));
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Manage Campus Library</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Upload New Resource</h2>
          <form className="space-y-4 mb-8">
            <div>
              <label htmlFor="resourceTitle" className="block text-gray-700 font-bold mb-2">Resource Title</label>
              <input type="text" id="resourceTitle" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div>
              <label htmlFor="resourceFile" className="block text-gray-700 font-bold mb-2">Resource File</label>
              <input type="file" id="resourceFile" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <Button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
              Upload Resource
            </Button>
          </form>

          <h2 className="text-2xl font-bold text-gray-900 mb-4">Existing Resources</h2>
          {resources.length > 0 ? (
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Title</TableHead>
                  <TableHead>File</TableHead>
                  <TableHead className="text-right">Actions</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {resources.map((resource) => (
                  <TableRow key={resource.id}>
                    <TableCell className="font-medium">{resource.title}</TableCell>
                    <TableCell>{resource.file}</TableCell>
                    <TableCell className="text-right">
                      <Button variant="ghost" size="sm" onClick={() => handleEdit(resource.id)} className="mr-2">
                        <Edit className="h-4 w-4" />
                      </Button>
                      <Button variant="destructive" size="sm" onClick={() => handleDelete(resource.id)}>
                        <Trash2 className="h-4 w-4" />
                      </Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          ) : (
            <p className="text-gray-600">No library resources uploaded yet.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default ManageLibrary;
