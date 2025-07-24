import React, { useState } from 'react';
import { Button } from '../components/ui/button';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table';
import { Edit, Trash2 } from 'lucide-react';

const ManageNotifications = () => {
  const [notifications, setNotifications] = useState([
    { id: 1, title: 'Admission Open', content: 'Admissions for 2025 are now open.' },
    { id: 2, title: 'Exam Schedule', content: 'Semester exam schedule released.' },
    { id: 3, title: 'Holiday Notice', content: 'College will be closed on 26th Jan.' },
  ]);

  const handleEdit = (id) => {
    console.log('Edit notification:', id);
    // In a real application, you would navigate to an edit page or open a modal
  };

  const handleDelete = (id) => {
    console.log('Delete notification:', id);
    setNotifications(notifications.filter(notification => notification.id !== id));
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Manage Notifications</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Create New Notification</h2>
          <form className="space-y-4 mb-8">
            <div>
              <label htmlFor="notificationTitle" className="block text-gray-700 font-bold mb-2">Title</label>
              <input type="text" id="notificationTitle" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" />
            </div>
            <div>
              <label htmlFor="notificationContent" className="block text-gray-700 font-bold mb-2">Content</label>
              <textarea id="notificationContent" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"></textarea>
            </div>
            <Button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">
              Publish Notification
            </Button>
          </form>

          <h2 className="text-2xl font-bold text-gray-900 mb-4">Existing Notifications</h2>
          {notifications.length > 0 ? (
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Title</TableHead>
                  <TableHead>Content</TableHead>
                  <TableHead className="text-right">Actions</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {notifications.map((notification) => (
                  <TableRow key={notification.id}>
                    <TableCell className="font-medium">{notification.title}</TableCell>
                    <TableCell>{notification.content}</TableCell>
                    <TableCell className="text-right">
                      <Button variant="ghost" size="sm" onClick={() => handleEdit(notification.id)} className="mr-2">
                        <Edit className="h-4 w-4" />
                      </Button>
                      <Button variant="destructive" size="sm" onClick={() => handleDelete(notification.id)}>
                        <Trash2 className="h-4 w-4" />
                      </Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          ) : (
            <p className="text-gray-600">No notifications published yet.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default ManageNotifications;
