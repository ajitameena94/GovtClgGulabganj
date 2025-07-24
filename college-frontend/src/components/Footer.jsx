import React from 'react';
import { Link } from 'react-router-dom';
import { MapPin, Phone, Mail, Clock, Facebook, Twitter, Instagram, Youtube } from 'lucide-react';
import collegeLogo from '../assets/college_logo.png';

const Footer = () => {
  const currentYear = new Date().getFullYear();

  const quickLinks = [
    { name: 'About College', href: '/about' },
    { name: 'Admissions', href: '/admissions' },
    { name: 'Academic Programs', href: '/academics/programs' },
    { name: 'Faculty', href: '/faculty' },
    { name: 'Results', href: '/results' },
    { name: 'Gallery', href: '/gallery' }
  ];

  const academicLinks = [
    { name: 'BA History', href: '/academics/programs/history' },
    { name: 'BA Economics', href: '/academics/programs/economics' },
    { name: 'BA Sociology', href: '/academics/programs/sociology' },
    { name: 'BA Political Science', href: '/academics/programs/political-science' },
    { name: 'BA Hindi Literature', href: '/academics/programs/hindi-literature' },
    { name: 'BA English Literature', href: '/academics/programs/english-literature' }
  ];

  const importantLinks = [
    { name: 'Notifications', href: '/notifications' },
    { name: 'Timetable', href: '/timetable' },
    { name: 'Student Portal', href: '/student-portal' },
    { name: 'Examination', href: '/academics/examination' },
    { name: 'Syllabus', href: '/academics/syllabus' },
    { name: 'Contact Us', href: '/contact' }
  ];

  return (
    <footer className="bg-primary text-primary-foreground">
      {/* Main Footer Content */}
      <div className="container mx-auto px-4 py-12">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {/* College Information */}
          <div className="space-y-4">
            <div className="flex items-center space-x-3">
              <img 
                src={collegeLogo} 
                alt="College Logo" 
                className="h-12 w-12 object-contain bg-white rounded-full p-1"
              />
              <div>
                <h3 className="text-lg font-bold">Govt. College Gulabganj</h3>
                <p className="text-sm opacity-90">Est. 2015</p>
              </div>
            </div>
            <p className="text-sm opacity-90 leading-relaxed">
              Government College of Gulabganj, Vidisha is committed to providing quality higher education 
              and fostering academic excellence in various disciplines of Arts and Humanities.
            </p>
            <div className="flex space-x-3">
              <a href="#" className="p-2 bg-white/10 rounded-full hover:bg-white/20 transition-colors">
                <Facebook className="h-4 w-4" />
              </a>
              <a href="#" className="p-2 bg-white/10 rounded-full hover:bg-white/20 transition-colors">
                <Twitter className="h-4 w-4" />
              </a>
              <a href="#" className="p-2 bg-white/10 rounded-full hover:bg-white/20 transition-colors">
                <Instagram className="h-4 w-4" />
              </a>
              <a href="#" className="p-2 bg-white/10 rounded-full hover:bg-white/20 transition-colors">
                <Youtube className="h-4 w-4" />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Quick Links</h3>
            <ul className="space-y-2">
              {quickLinks.map((link) => (
                <li key={link.name}>
                  <Link 
                    to={link.href} 
                    className="text-sm opacity-90 hover:opacity-100 hover:text-secondary transition-all"
                  >
                    {link.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Academic Programs */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Academic Programs</h3>
            <ul className="space-y-2">
              {academicLinks.map((link) => (
                <li key={link.name}>
                  <Link 
                    to={link.href} 
                    className="text-sm opacity-90 hover:opacity-100 hover:text-secondary transition-all"
                  >
                    {link.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact Information */}
          <div className="space-y-4">
            <h3 className="text-lg font-semibold">Contact Information</h3>
            <div className="space-y-3">
              <div className="flex items-start space-x-3">
                <MapPin className="h-5 w-5 mt-0.5 flex-shrink-0" />
                <div>
                  <p className="text-sm opacity-90">
                    Government Higher Secondary School Campus<br />
                    Gulabganj, District Vidisha<br />
                    Madhya Pradesh - 464220
                  </p>
                </div>
              </div>
              
              <div className="flex items-center space-x-3">
                <Phone className="h-5 w-5 flex-shrink-0" />
                <p className="text-sm opacity-90">+91 98264 58553</p>
              </div>
              
              <div className="flex items-center space-x-3">
                <Mail className="h-5 w-5 flex-shrink-0" />
                <p className="text-sm opacity-90">hegcgulvid@mp.gov.in</p>
              </div>
              
              <div className="flex items-start space-x-3">
                <Clock className="h-5 w-5 mt-0.5 flex-shrink-0" />
                <div>
                  <p className="text-sm opacity-90">
                    Mon - Fri: 9:00 AM - 5:00 PM<br />
                    Sat: 9:00 AM - 1:00 PM<br />
                    Sun: Closed
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Important Links Bar */}
      <div className="border-t border-white/20">
        <div className="container mx-auto px-4 py-4">
          <div className="flex flex-wrap justify-center gap-4 md:gap-8">
            {importantLinks.map((link) => (
              <Link
                key={link.name}
                to={link.href}
                className="text-sm opacity-90 hover:opacity-100 hover:text-secondary transition-all"
              >
                {link.name}
              </Link>
            ))}
          </div>
        </div>
      </div>

      {/* Bottom Bar */}
      <div className="border-t border-white/20">
        <div className="container mx-auto px-4 py-4">
          <div className="flex flex-col md:flex-row justify-between items-center space-y-2 md:space-y-0">
            <p className="text-sm opacity-90">
              © {currentYear} Government College of Gulabganj, Vidisha. All rights reserved.
            </p>
            <div className="flex items-center space-x-4 text-sm opacity-90">
              <Link to="/privacy-policy" className="hover:opacity-100 transition-opacity">
                Privacy Policy
              </Link>
              <span>|</span>
              <Link to="/terms-conditions" className="hover:opacity-100 transition-opacity">
                Terms & Conditions
              </Link>
              <span>|</span>
              <Link to="/sitemap" className="hover:opacity-100 transition-opacity">
                Sitemap
              </Link>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;

