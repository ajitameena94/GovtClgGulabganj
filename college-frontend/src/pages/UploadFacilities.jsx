import React from 'react';
import { Link } from 'react-router-dom';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Button } from '../components/ui/button';
import { Upload, Users, FileText, CalendarDays } from 'lucide-react';

const UploadFacilities = () => {
  const uploadOptions = [
    {
      title: 'Upload Gallery Images',
      description: 'Add new images to the college gallery.',
      icon: Upload,
      link: '/admin/upload/gallery',
    },
    {
      title: 'Bulk Upload Faculty',
      description: 'Upload faculty data in bulk via a CSV/Excel file.',
      icon: Users,
      link: '/admin/upload/faculty', // Placeholder link
    },
    {
      title: 'Bulk Upload Results',
      description: 'Upload student results in bulk.',
      icon: FileText,
      link: '/admin/upload/results', // Placeholder link
    },
    {
      title: 'Bulk Upload Timetables',
      description: 'Upload class timetables in bulk.',
      icon: CalendarDays,
      link: '/admin/upload/timetables', // Placeholder link
    },
  ];

  return (
    <div className="min-h-screen bg-gray-100 py-20 px-4">
      <div className="container mx-auto">
        <h1 className="text-4xl font-bold text-center text-gray-900 mb-10">Upload Facilities</h1>
        <p className="text-center text-lg text-gray-600 mb-12">
          Manage and upload various types of data to the college system.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {uploadOptions.map((option, index) => (
            <Card key={index} className="flex flex-col justify-between card-hover">
              <CardHeader>
                <div className="flex items-center space-x-4 mb-4">
                  <div className="p-3 bg-primary/10 rounded-lg">
                    <option.icon className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl font-semibold">{option.title}</CardTitle>
                </div>
                <p className="text-gray-600 text-sm">{option.description}</p>
              </CardHeader>
              <CardContent>
                <Link to={option.link}>
                  <Button className="w-full mt-4">Go to {option.title}</Button>
                </Link>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </div>
  );
};

export default UploadFacilities;
