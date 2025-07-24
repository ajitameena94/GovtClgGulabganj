import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { 
  BookOpen, 
  Users, 
  Award, 
  Calendar,
  Bell,
  FileText,
  Clock,
  MapPin,
  ChevronRight,
  GraduationCap,
  Building,
  Star
} from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../components/ui/card';
import { Badge } from '../components/ui/badge';
import '../App.css';

const Home = () => {
  const [notifications, setNotifications] = useState([]);
  const [featuredGallery, setFeaturedGallery] = useState([]);

  // Mock data - in real app, this would come from API
  useEffect(() => {
    // Mock notifications
    const unsortedNotifications = [
      {
        id: 1,
        title: 'Admission Open for Session 2024-25',
        category: 'admission',
        priority: 'high',
        created_at: '2024-01-15T10:00:00Z'
      },
      {
        id: 2,
        title: 'Semester Examination Schedule Released',
        category: 'exam',
        priority: 'normal',
        created_at: '2024-01-14T14:30:00Z'
      },
      {
        id: 3,
        title: 'Annual Cultural Function - 2024',
        category: 'event',
        priority: 'normal',
        created_at: '2024-01-13T09:15:00Z'
      }
    ];
    setNotifications(unsortedNotifications.sort((a, b) => new Date(b.created_at) - new Date(a.created_at)));

    // Mock gallery items
    setFeaturedGallery([
      {
        id: 1,
        title: 'College Campus',
        image_url: 'https://images.unsplash.com/photo-1562774053-701939374585?w=400&h=300&fit=crop',
        category: 'infrastructure'
      },
      {
        id: 2,
        title: 'Annual Function 2023',
        image_url: 'https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=400&h=300&fit=crop',
        category: 'events'
      },
      {
        id: 3,
        title: 'Library',
        image_url: 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=400&h=300&fit=crop',
        category: 'infrastructure'
      }
    ]);
  }, []);

  const quickAccessItems = [
    {
      title: 'Check Results',
      description: 'View semester examination results',
      icon: FileText,
      href: '/results',
      color: 'bg-blue-500'
    },
    {
      title: 'Timetable',
      description: 'Class schedules and timings',
      icon: Clock,
      href: '/timetable',
      color: 'bg-green-500'
    },
    {
      title: 'Notifications',
      description: 'Latest announcements',
      icon: Bell,
      href: '/notifications',
      color: 'bg-orange-500'
    },
    {
      title: 'Admissions',
      description: 'Apply for admission',
      icon: GraduationCap,
      href: '/admissions',
      color: 'bg-purple-500'
    }
  ];

  const baPrograms = [
    {
      name: 'BA History',
      description: 'Explore the rich tapestry of human civilization and historical events.',
      duration: '3 Years',
      icon: BookOpen
    },
    {
      name: 'BA Economics',
      description: 'Understand economic principles and their real-world applications.',
      duration: '3 Years',
      icon: Award
    },
    {
      name: 'BA Sociology',
      description: 'Study society, social relationships, and human behavior patterns.',
      duration: '3 Years',
      icon: Users
    },
    {
      name: 'BA Political Science',
      description: 'Analyze political systems, governance, and public policy.',
      duration: '3 Years',
      icon: Building
    },
    {
      name: 'BA Hindi Literature',
      description: 'Delve into the beauty and depth of Hindi literary traditions.',
      duration: '3 Years',
      icon: BookOpen
    },
    {
      name: 'BA English Literature',
      description: 'Explore English literary works and develop critical thinking skills.',
      duration: '3 Years',
      icon: BookOpen
    }
  ];

  const collegeStats = [
    { label: 'Years of Excellence', value: '9+', icon: Star },
    { label: 'Students Enrolled', value: '500+', icon: Users },
    { label: 'Faculty Members', value: '25+', icon: GraduationCap },
    { label: 'BA Programs', value: '6', icon: BookOpen }
  ];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="hero-gradient text-white py-20 relative overflow-hidden">
        <div className="absolute inset-0 bg-black/20"></div>
        <div className="container mx-auto px-4 relative z-10">
          <div className="max-w-4xl mx-auto text-center animate-fade-in">
            <h1 className="text-4xl md:text-6xl font-bold mb-6">
              Welcome to <span className="text-secondary">Govt. College Gulabganj</span>
            </h1>
            <p className="text-xl md:text-2xl mb-8 opacity-90">
              Empowering minds, shaping futures since 2015
            </p>
            <p className="text-lg mb-10 opacity-80 max-w-2xl mx-auto">
              Discover excellence in higher education with our comprehensive BA programs 
              in History, Economics, Sociology, Political Science, Hindi Literature, and English Literature.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link to="/admissions">
                <Button size="lg" variant="secondary" className="text-lg px-8 py-3">
                  Apply Now
                  <ChevronRight className="ml-2 h-5 w-5" />
                </Button>
              </Link>
              <Link to="/about">
                <Button size="lg" variant="outline" className="text-lg px-8 py-3 border-white text-white hover:bg-white hover:text-primary">
                  Learn More
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Latest Notifications & Gallery */}
      <section className="py-16 bg-gray-50">
        <div className="container mx-auto px-4">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
            {/* Notifications */}
            <div>
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-2xl font-bold text-gray-900">Latest Notifications</h2>
                <Link to="/notifications">
                  <Button variant="outline" size="sm">
                    View All
                    <ChevronRight className="ml-2 h-4 w-4" />
                  </Button>
                </Link>
              </div>
              
              <div className="space-y-4">
                {notifications.map((notification) => (
                  <Card key={notification.id} className="card-hover">
                    <CardContent className="p-4">
                      <div className="flex items-start justify-between">
                        <div className="flex-1">
                          <div className="flex items-center space-x-2 mb-2">
                            <Badge 
                              variant={notification.priority === 'high' ? 'destructive' : 'secondary'}
                              className="text-xs"
                            >
                              {notification.category}
                            </Badge>
                            <span className="text-xs text-gray-500">
                              {new Date(notification.created_at).toLocaleDateString()}
                            </span>
                          </div>
                          <h3 className="font-semibold text-gray-900 mb-1">
                            {notification.title}
                          </h3>
                        </div>
                        <Bell className="h-5 w-5 text-gray-400 flex-shrink-0" />
                      </div>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </div>

            {/* Featured Gallery */}
            <div>
              <div className="flex items-center justify-between mb-6">
                <h2 className="text-2xl font-bold text-gray-900">Campus Gallery</h2>
                <Link to="/gallery">
                  <Button variant="outline" size="sm">
                    View All
                    <ChevronRight className="ml-2 h-4 w-4" />
                  </Button>
                </Link>
              </div>
              
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {featuredGallery.map((item) => (
                  <div key={item.id} className="relative group overflow-hidden rounded-lg">
                    <img 
                      src={item.image_url} 
                      alt={item.title}
                      className="w-full h-48 object-cover transition-transform group-hover:scale-110"
                    />
                    <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity">
                      <div className="absolute bottom-4 left-4 text-white">
                        <h3 className="font-semibold">{item.title}</h3>
                        <p className="text-sm opacity-90">{item.category}</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Quick Access Section */}
      <section className="py-16 bg-gray-50">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Quick Access</h2>
            <p className="text-lg text-gray-600">Get instant access to important resources</p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {quickAccessItems.map((item, index) => (
              <Link key={index} to={item.href}>
                <Card className="card-hover cursor-pointer h-full">
                  <CardContent className="p-6 text-center">
                    <div className={`${item.color} w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4`}>
                      <item.icon className="h-8 w-8 text-white" />
                    </div>
                    <h3 className="text-lg font-semibold mb-2">{item.title}</h3>
                    <p className="text-gray-600 text-sm">{item.description}</p>
                  </CardContent>
                </Card>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* BA Programs Section */}
      <section className="py-16">
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">Our BA Programs</h2>
            <p className="text-lg text-gray-600 max-w-2xl mx-auto">
              Choose from our diverse range of Bachelor of Arts programs designed to provide 
              comprehensive knowledge and skills in various disciplines.
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {baPrograms.map((program, index) => (
              <Card key={index} className="card-hover">
                <CardHeader>
                  <div className="flex items-center space-x-3 mb-2">
                    <div className="p-2 bg-primary/10 rounded-lg">
                      <program.icon className="h-6 w-6 text-primary" />
                    </div>
                    <Badge variant="secondary">{program.duration}</Badge>
                  </div>
                  <CardTitle className="text-xl">{program.name}</CardTitle>
                </CardHeader>
                <CardContent>
                  <CardDescription className="text-base mb-4">
                    {program.description}
                  </CardDescription>
                  <Link to="/academics/programs">
                    <Button variant="outline" size="sm">
                      Learn More
                      <ChevronRight className="ml-2 h-4 w-4" />
                    </Button>
                  </Link>
                </CardContent>
              </Card>
            ))}
          </div>
          
          <div className="text-center mt-10">
            <Link to="/academics/programs">
              <Button size="lg">
                View All Programs
                <ChevronRight className="ml-2 h-5 w-5" />
              </Button>
            </Link>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section className="py-16">
        <div className="container mx-auto px-4">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-3xl font-bold text-gray-900 mb-6">About Our College</h2>
              <p className="text-lg text-gray-600 mb-6 leading-relaxed">
                Government College of Gulabganj, Vidisha, established in 2015, is a premier 
                institution dedicated to providing quality higher education in the field of 
                Arts and Humanities. Located in the historic district of Vidisha, Madhya Pradesh, 
                our college has been serving the educational needs of the region with commitment and excellence.
              </p>
              <p className="text-lg text-gray-600 mb-8 leading-relaxed">
                We offer comprehensive Bachelor of Arts programs in six major disciplines, 
                fostering critical thinking, creativity, and academic excellence among our students. 
                Our experienced faculty and modern infrastructure create an ideal learning environment 
                for holistic development.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <Link to="/about">
                  <Button size="lg">
                    Learn More About Us
                    <ChevronRight className="ml-2 h-5 w-5" />
                  </Button>
                </Link>
                <Link to="/contact">
                  <Button variant="outline" size="lg">
                    Contact Us
                  </Button>
                </Link>
              </div>
            </div>
            
            <div className="relative">
               <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3660.832295965443!2d77.9133564149757!3d23.61019258474883!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39792b1b7e8d8b1b%3A0x4f0d6a29e8d8b1b!2sGovt.%20College%20Gulabganj!5e0!3m2!1sen!2sin!4v1678886425628!5m2!1sen!2sin"
                width="600" 
                height="450" 
                style={{ border: 0 }} 
                allowFullScreen="" 
                loading="lazy" 
                referrerPolicy="no-referrer-when-downgrade"
                className="rounded-lg shadow-lg w-full"
              ></iframe>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;

