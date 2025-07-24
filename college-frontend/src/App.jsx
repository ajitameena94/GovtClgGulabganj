import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import AdminLogin from './pages/AdminLogin';
import AdminDashboard from './pages/AdminDashboard';
import UploadFacilities from './pages/UploadFacilities';
import UploadGallery from './pages/UploadGallery';
import ManageLibrary from './pages/ManageLibrary';
import ManageNotifications from './pages/ManageNotifications';
import ManageTimetables from './pages/ManageTimetables';
import ManageGallery from './pages/ManageGallery';
import ProtectedRoute from './components/ProtectedRoute';
import About from './pages/About';
import Academics from './pages/Academics';
import Admissions from './pages/Admissions';
import Contact from './pages/Contact';
import Faculty from './pages/Faculty';
import Gallery from './pages/Gallery';
import Notifications from './pages/Notifications';
import Results from './pages/Results';
import Timetable from './pages/Timetable';
import './App.css';

function App() {
  return (
    <Router basename="/GovtClgGulabganj">
      <div className="min-h-screen flex flex-col">
        <Header />
        <main className="flex-1">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/academics" element={<Academics />} />
            <Route path="/admissions" element={<Admissions />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/faculty" element={<Faculty />} />
            <Route path="/gallery" element={<Gallery />} />
            <Route path="/notifications" element={<Notifications />} />
            <Route path="/results" element={<Results />} />
            <Route path="/timetable" element={<Timetable />} />
            <Route path="/admin/login" element={<AdminLogin />} />
            <Route 
              path="/admin"
              element={
                <ProtectedRoute>
                  <AdminDashboard />
                </ProtectedRoute>
              }
            />
            <Route 
              path="/admin/upload-facilities"
              element={
                <ProtectedRoute>
                  <UploadFacilities />
                </ProtectedRoute>
              }
            />
            <Route 
              path="/admin/upload/gallery"
              element={
                <ProtectedRoute>
                  <UploadGallery />
                </ProtectedRoute>
              }
            />
            <Route 
              path="/admin/manage-library"
              element={
                <ProtectedRoute>
                  <ManageLibrary />
                </ProtectedRoute>
              }
            />
            <Route 
              path="/admin/manage-notifications"
              element={
                <ProtectedRoute>
                  <ManageNotifications />
                </ProtectedRoute>
              }
            />
            <Route 
              path="/admin/manage-timetables"
              element={
                <ProtectedRoute>
                  <ManageTimetables />
                </ProtectedRoute>
              }
            />
            <Route 
              path="/admin/manage-gallery"
              element={
                <ProtectedRoute>
                  <ManageGallery />
                </ProtectedRoute>
              }
            />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;

