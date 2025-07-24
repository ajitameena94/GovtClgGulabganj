import React, { useState, useEffect } from 'react';
import { Button } from '../components/ui/button';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '../components/ui/table';
import { Edit, Trash2 } from 'lucide-react';

const ManageNotifications = () => {
  const [notifications, setNotifications] = useState([]);
  const [newNotificationTitle, setNewNotificationTitle] = useState('');
  const [newNotificationContent, setNewNotificationContent] = useState('');

  const fetchNotifications = async () => {
    try {
      const response = await fetch('/api/notifications');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      setNotifications(data.sort((a, b) => new Date(b.created_at) - new Date(a.created_at)));
    } catch (error) {
      console.error("Error fetching notifications:", error);
    }
  };

  useEffect(() => {
    fetchNotifications();
  }, []);

  const handleAddNotification = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/notifications', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: newNotificationTitle,
          content: newNotificationContent,
        }),
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      setNewNotificationTitle('');
      setNewNotificationContent('');
      fetchNotifications(); // Refresh the list
    } catch (error) {
      console.error("Error adding notification:", error);
    }
  };

  const handleEdit = (id) => {
    console.log('Edit notification:', id);
    // In a real application, you would navigate to an edit page or open a modal
  };

  const handleDelete = async (id) => {
    try {
      const response = await fetch(`/api/notifications/${id}`, {
        method: 'DELETE',
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      fetchNotifications(); // Refresh the list
    } catch (error) {
      console.error("Error deleting notification:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Manage Notifications</h1>
        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Create New Notification</h2>
          <form onSubmit={handleAddNotification} className="space-y-4 mb-8">
            <div>
              <label htmlFor="notificationTitle" className="block text-gray-700 font-bold mb-2">Title</label>
              <input type="text" id="notificationTitle" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" value={newNotificationTitle} onChange={(e) => setNewNotificationTitle(e.target.value)} required />
            </div>
            <div>
              <label htmlFor="notificationContent" className="block text-gray-700 font-bold mb-2">Content</label>
              <textarea id="notificationContent" className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" value={newNotificationContent} onChange={(e) => setNewNotificationContent(e.target.value)} required></textarea>
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
