import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Menu, X, ChevronDown } from 'lucide-react';
import { Button } from './ui/button';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from './ui/dropdown-menu';
import collegeLogo from '../assets/college_logo.png';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const location = useLocation();

  const navigation = [
    { name: 'Home', href: '/' },
    { 
      name: 'About', 
      href: '/about',
      dropdown: [
        { name: 'About College', href: '/about' },
        { name: 'Vision & Mission', href: '/about/vision-mission' },
        { name: 'Principal Message', href: '/about/principal-message' },
        { name: 'History', href: '/about/history' }
      ]
    },
    { 
      name: 'Academics', 
      href: '/academics',
      dropdown: [
        { name: 'BA Programs', href: '/academics/programs' },
        { name: 'Syllabus', href: '/academics/syllabus' },
        { name: 'Examination', href: '/academics/examination' },
        { name: 'Academic Calendar', href: '/academics/calendar' }
      ]
    },
    { 
      name: 'Faculty', 
      href: '/faculty',
      dropdown: [
        { name: 'All Faculty', href: '/faculty' },
        { name: 'History Department', href: '/faculty/history' },
        { name: 'Economics Department', href: '/faculty/economics' },
        { name: 'Political Science', href: '/faculty/political-science' },
        { name: 'Sociology', href: '/faculty/sociology' },
        { name: 'Literature', href: '/faculty/literature' }
      ]
    },
    { name: 'Admissions', href: '/admissions' },
    { name: 'Results', href: '/results' },
    { name: 'Gallery', href: '/gallery' },
    { name: 'Contact', href: '/contact' }
  ];

  const isActive = (href) => {
    if (href === '/') {
      return location.pathname === '/';
    }
    return location.pathname.startsWith(href);
  };

  return (
    <header className="bg-white shadow-lg sticky top-0 z-50">
      {/* Top Bar */}
      <div className="bg-primary text-primary-foreground py-2">
        <div className="container mx-auto px-4">
          <div className="flex justify-between items-center text-sm">
            <div className="flex items-center space-x-4">
              <span>📧 hegcgulvid@mp.gov.in</span>
              <span>📞 +91 98264 58553</span>
            </div>
            <div className="flex items-center space-x-4">
              <Link to="/student-portal" className="hover:text-secondary transition-colors">
                Student Portal
              </Link>
              <Link to="/admin" className="hover:text-secondary transition-colors">
                Admin Login
              </Link>
            </div>
          </div>
        </div>
      </div>

      {/* Main Header */}
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between py-4">
          {/* Logo and College Name */}
          <Link to="/" className="flex items-center space-x-4">
            <img 
              src={collegeLogo} 
              alt="Govt. College Gulabganj Logo" 
              className="h-16 w-16 object-contain"
            />
            <div className="hidden md:block">
              <h1 className="text-2xl font-bold text-primary">
                Govt. College Gulabganj
              </h1>
              <p className="text-sm text-muted-foreground">
                Vidisha, Madhya Pradesh • Est. 2015
              </p>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden lg:flex items-center space-x-1">
            {navigation.map((item) => (
              <div key={item.name} className="relative">
                {item.dropdown ? (
                  <DropdownMenu>
                    <DropdownMenuTrigger asChild>
                      <Button
                        variant="ghost"
                        className={`flex items-center space-x-1 ${
                          isActive(item.href) 
                            ? 'text-primary bg-primary/10' 
                            : 'text-foreground hover:text-primary'
                        }`}
                      >
                        <span>{item.name}</span>
                        <ChevronDown className="h-4 w-4" />
                      </Button>
                    </DropdownMenuTrigger>
                    <DropdownMenuContent align="start" className="w-56">
                      {item.dropdown.map((dropdownItem) => (
                        <DropdownMenuItem key={dropdownItem.name} asChild>
                          <Link 
                            to={dropdownItem.href}
                            className="w-full cursor-pointer"
                          >
                            {dropdownItem.name}
                          </Link>
                        </DropdownMenuItem>
                      ))}
                    </DropdownMenuContent>
                  </DropdownMenu>
                ) : (
                  <Link
                    to={item.href}
                    className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                      isActive(item.href)
                        ? 'text-primary bg-primary/10'
                        : 'text-foreground hover:text-primary hover:bg-primary/5'
                    }`}
                  >
                    {item.name}
                  </Link>
                )}
              </div>
            ))}
          </nav>

          {/* Quick Actions */}
          <div className="hidden md:flex items-center space-x-2">
            <Link to="/notifications">
              <Button variant="outline" size="sm">
                Notifications
              </Button>
            </Link>
            <Link to="/timetable">
              <Button variant="outline" size="sm">
                Timetable
              </Button>
            </Link>
          </div>

          {/* Mobile Menu Button */}
          <Button
            variant="ghost"
            size="sm"
            className="lg:hidden"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            {isMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </Button>
        </div>
      </div>

      {/* Mobile Navigation */}
      {isMenuOpen && (
        <div className="lg:hidden bg-white border-t">
          <div className="container mx-auto px-4 py-4">
            <nav className="space-y-2">
              {navigation.map((item) => (
                <div key={item.name}>
                  <Link
                    to={item.href}
                    className={`block px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                      isActive(item.href)
                        ? 'text-primary bg-primary/10'
                        : 'text-foreground hover:text-primary hover:bg-primary/5'
                    }`}
                    onClick={() => setIsMenuOpen(false)}
                  >
                    {item.name}
                  </Link>
                  {item.dropdown && (
                    <div className="ml-4 mt-1 space-y-1">
                      {item.dropdown.map((dropdownItem) => (
                        <Link
                          key={dropdownItem.name}
                          to={dropdownItem.href}
                          className="block px-3 py-1 text-sm text-muted-foreground hover:text-primary transition-colors"
                          onClick={() => setIsMenuOpen(false)}
                        >
                          {dropdownItem.name}
                        </Link>
                      ))}
                    </div>
                  )}
                </div>
              ))}
              
              {/* Mobile Quick Actions */}
              <div className="pt-4 border-t space-y-2">
                <Link to="/notifications" onClick={() => setIsMenuOpen(false)}>
                  <Button variant="outline" size="sm" className="w-full">
                    Notifications
                  </Button>
                </Link>
                <Link to="/timetable" onClick={() => setIsMenuOpen(false)}>
                  <Button variant="outline" size="sm" className="w-full">
                    Timetable
                  </Button>
                </Link>
                <Link to="/student-portal" onClick={() => setIsMenuOpen(false)}>
                  <Button variant="outline" size="sm" className="w-full">
                    Student Portal
                  </Button>
                </Link>
              </div>
            </nav>
          </div>
        </div>
      )}
    </header>
  );
};

export default Header;

