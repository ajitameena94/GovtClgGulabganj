import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import './App.css';

// Placeholder components for other pages
const About = () => <div className="min-h-screen py-20 px-4"><div className="container mx-auto"><h1 className="text-4xl font-bold text-center">About Us</h1><p className="text-center mt-4 text-gray-600">About page coming soon...</p></div></div>;
const Academics = () => <div className="min-h-screen py-20 px-4"><div className="container mx-auto"><h1 className="text-4xl font-bold text-center">Academics</h1><p className="text-center mt-4 text-gray-600">Academics page coming soon...</p></div></div>;
const Faculty = () => <div className="min-h-screen py-20 px-4"><div className="container mx-auto"><h1 className="text-4xl font-bold text-center">Faculty</h1><p className="text-center mt-4 text-gray-600">Faculty page coming soon...</p></div></div>;
const Admissions = () => <div className="min-h-screen py-20 px-4"><div className="container mx-auto"><h1 className="text-4xl font-bold text-center">Admissions</h1><p className="text-center mt-4 text-gray-600">Admissions page coming soon...</p></div></div>;
const Results = () => <div className="min-h-screen py-20 px-4"><div className="container mx-auto"><h1 className="text-4xl font-bold text-center">Results</h1><p className="text-center mt-4 text-gray-600">Results page coming soon...</p></div></div>;
const Gallery = () => <div className="min-h-screen py-20 px-4"><div className="container mx-auto"><h1 className="text-4xl font-bold text-center">Gallery</h1><p className="text-center mt-4 text-gray-600">Gallery page coming soon...</p></div></div>;
const Contact = () => <div className="min-h-screen py-20 px-4"><div className="container mx-auto"><h1 className="text-4xl font-bold text-center">Contact Us</h1><p className="text-center mt-4 text-gray-600">Contact page coming soon...</p></div></div>;
const Notifications = () => <div className="min-h-screen py-20 px-4"><div className="container mx-auto"><h1 className="text-4xl font-bold text-center">Notifications</h1><p className="text-center mt-4 text-gray-600">Notifications page coming soon...</p></div></div>;
const Timetable = () => <div className="min-h-screen py-20 px-4"><div className="container mx-auto"><h1 className="text-4xl font-bold text-center">Timetable</h1><p className="text-center mt-4 text-gray-600">Timetable page coming soon...</p></div></div>;
const StudentPortal = () => <div className="min-h-screen py-20 px-4"><div className="container mx-auto"><h1 className="text-4xl font-bold text-center">Student Portal</h1><p className="text-center mt-4 text-gray-600">Student Portal coming soon...</p></div></div>;
const Admin = () => <div className="min-h-screen py-20 px-4"><div className="container mx-auto"><h1 className="text-4xl font-bold text-center">Admin Login</h1><p className="text-center mt-4 text-gray-600">Admin panel coming soon...</p></div></div>;

function App() {
  return (
    <Router>
      <div className="min-h-screen flex flex-col">
        <Header />
        <main className="flex-1">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/about/*" element={<About />} />
            <Route path="/academics" element={<Academics />} />
            <Route path="/academics/*" element={<Academics />} />
            <Route path="/faculty" element={<Faculty />} />
            <Route path="/faculty/*" element={<Faculty />} />
            <Route path="/admissions" element={<Admissions />} />
            <Route path="/results" element={<Results />} />
            <Route path="/gallery" element={<Gallery />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/notifications" element={<Notifications />} />
            <Route path="/timetable" element={<Timetable />} />
            <Route path="/student-portal" element={<StudentPortal />} />
            <Route path="/admin" element={<Admin />} />
            <Route path="/privacy-policy" element={<About />} />
            <Route path="/terms-conditions" element={<About />} />
            <Route path="/sitemap" element={<About />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;

