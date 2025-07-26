import React from 'react';
import { Link } from 'react-router-dom';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Button } from '../components/ui/button';
import { Book, Bell, CalendarDays, Image, Upload } from 'lucide-react';

const AdminDashboard = () => {
  const adminActions = [
    {
      title: 'Manage Notifications',
      description: 'Create, edit, and delete college notifications.',
      icon: Bell,
      link: '/admin/manage-notifications',
    },
    {
      title: 'Manage Timetables',
      description: 'Upload and manage class timetables.',
      icon: CalendarDays,
      link: '/admin/manage-timetables',
    },
    {
      title: 'Upload Gallery',
      description: 'Upload, view, edit, and delete campus gallery images.',
      icon: Image,
      link: '/admin/upload/gallery',
    },
    {
      title: 'Manage Results',
      description: 'Upload and manage academic results.',
      icon: Book,
      link: '/admin/manage-results',
    },
  ];

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Admin Dashboard</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {adminActions.map((action, index) => (
            <Card key={index} className="card-hover">
              <CardHeader>
                <CardTitle className="flex items-center space-x-2">
                  <action.icon className="h-6 w-6 text-primary" />
                  <span>{action.title}</span>
                </CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-gray-600 mb-4">{action.description}</p>
                <Link to={action.link}>
                  <Button>Go to {action.title}</Button>
                </Link>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;