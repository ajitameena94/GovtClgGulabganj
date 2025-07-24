import React, { useState } from 'react';
import { Button } from '../components/ui/button';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table';
import { Edit, Trash2 } from 'lucide-react';

const ManageTimetables = () => {
  const [timetables, setTimetables] = useState([
    { id: 1, title: 'BA 1st Year Timetable', file: 'ba1_timetable.pdf' },
    { id: 2, title: 'BA 2nd Year Timetable', file: 'ba2_timetable.pdf' },
    { id: 3, title: 'BA 3rd Year Timetable', file: 'ba3_timetable.pdf' },
  ]);

  const handleEdit = (id) => {
    console.log('Edit timetable:', id);
    // In a real application, you would navigate to an edit page or open a modal
  };

  const handleDelete = async (id) => {
    console.log('Delete timetable:', id);
    try {
      const response = await fetch(`https://college-backend-api.onrender.com/api/timetables/${id}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`,
        },
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      setTimetables(timetables.filter(timetable => timetable.id !== id));
    } catch (error) {
      console.error("Error deleting timetable:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Manage Timetables</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Upload New Timetable</h2>
          <form className="space-y-4 mb-8">
            <div>
              <label htmlFor="timetableTitle" className="block text-gray-700 font-bold mb-2">Timetable Title</label>
              <input type="text" id="timetableTitle" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div>
              <label htmlFor="timetableFile" className="block text-gray-700 font-bold mb-2">Timetable File (PDF/Image)</label>
              <input type="file" id="timetableFile" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <Button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
              Upload Timetable
            </Button>
          </form>

          <h2 className="text-2xl font-bold text-gray-900 mb-4">Existing Timetables</h2>
          {timetables.length > 0 ? (
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Title</TableHead>
                  <TableHead>File</TableHead>
                  <TableHead className="text-right">Actions</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {timetables.map((timetable) => (
                  <TableRow key={timetable.id}>
                    <TableCell className="font-medium">{timetable.title}</TableCell>
                    <TableCell>{timetable.file}</TableCell>
                    <TableCell className="text-right">
                      <Button variant="ghost" size="sm" onClick={() => handleEdit(timetable.id)} className="mr-2">
                        <Edit className="h-4 w-4" />
                      </Button>
                      <Button variant="destructive" size="sm" onClick={() => handleDelete(timetable.id)}>
                        <Trash2 className="h-4 w-4" />
                      </Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          ) : (
            <p className="text-gray-600">No timetables uploaded yet.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default ManageTimetables;
