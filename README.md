# Government College of Gulabganj Vidisha - Official Website

A comprehensive college management website built with React (frontend) and Flask (backend) for Government College of Gulabganj, Vidisha, Madhya Pradesh.

## 🎓 About the College

Government College of Gulabganj, established in 2015, is a premier institution dedicated to providing quality higher education in Arts and Humanities. The college offers Bachelor of Arts programs in six major disciplines:

- **BA History** - Ancient and Medieval Indian History
- **BA Economics** - Micro and Macroeconomics
- **BA Sociology** - Social Theory and Research Methods
- **BA Political Science** - Indian Government and Comparative Politics
- **BA Hindi Literature** - Classical and Modern Hindi Literature
- **BA English Literature** - Literary Analysis and Critical Thinking

## 🚀 Features

### 📱 Frontend (React)
- **Responsive Design** - Works on desktop, tablet, and mobile devices
- **Modern UI/UX** - Clean, professional design with college branding
- **Navigation System** - Comprehensive menu with dropdown options
- **Home Page** - Hero section, quick access, program showcase
- **Information Pages** - About, Academics, Faculty, Admissions
- **Interactive Elements** - Notifications, gallery, contact forms

### 🔧 Backend (Flask)
- **RESTful API** - Complete CRUD operations for all entities
- **Database Management** - SQLite database with proper relationships
- **Authentication System** - Admin login and session management
- **File Upload System** - Image and document upload functionality
- **CORS Support** - Cross-origin requests enabled for frontend integration

### 📊 Management Systems
- **Student Management** - Enrollment, records, and academic tracking
- **Faculty Management** - Staff profiles, departments, and qualifications
- **Notifications System** - Announcements, events, and important notices
- **Results Management** - Semester results and grade tracking
- **Timetable Management** - Class schedules and room assignments
- **Gallery System** - Photo uploads for events and infrastructure

## 🛠 Technology Stack

### Frontend
- **React 18** - Modern JavaScript framework
- **React Router** - Client-side routing
- **Tailwind CSS** - Utility-first CSS framework
- **Shadcn/UI** - High-quality UI components
- **Lucide Icons** - Beautiful icon library
- **Vite** - Fast build tool and development server

### Backend
- **Flask** - Python web framework
- **SQLAlchemy** - Database ORM
- **Flask-CORS** - Cross-origin resource sharing
- **SQLite** - Lightweight database
- **Werkzeug** - File upload handling

## 📁 Project Structure

```
GovtClgGulabgabj/
├── college-frontend/          # React frontend application
│   ├── src/
│   │   ├── components/        # Reusable UI components
│   │   ├── pages/            # Page components
│   │   ├── assets/           # Images and static files
│   │   └── App.jsx           # Main application component
│   ├── public/               # Public assets
│   └── package.json          # Frontend dependencies
├── college-backend/          # Flask backend application
│   ├── src/
│   │   ├── models/           # Database models
│   │   ├── routes/           # API route handlers
│   │   ├── static/           # Static file serving
│   │   └── main.py           # Application entry point
│   ├── venv/                 # Python virtual environment
│   └── requirements.txt      # Backend dependencies
├── README.md                 # This file
└── deployment-guide.md       # Deployment instructions
```

## 🚀 Quick Start

### Prerequisites
- Node.js (v18 or higher)
- Python (v3.8 or higher)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ajitameena94/GovtClgGulabgabj.git
   cd GovtClgGulabgabj
   ```

2. **Setup Backend**
   ```bash
   cd college-backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python src/seed_data.py   # Populate sample data
   python src/main.py        # Start backend server
   ```

3. **Setup Frontend**
   ```bash
   cd college-frontend
   npm install               # or pnpm install
   npm run dev              # Start development server
   ```

4. **Access the Application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:5000

### Default Admin Credentials
- **Username:** admin
- **Password:** admin123

## 📖 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### Authentication
- `POST /auth/login` - Admin login
- `POST /auth/logout` - Admin logout

#### Students
- `GET /students` - Get all students
- `POST /students` - Create new student
- `GET /students/{id}` - Get student by ID
- `PUT /students/{id}` - Update student
- `DELETE /students/{id}` - Delete student

#### Faculty
- `GET /faculty` - Get all faculty members
- `POST /faculty` - Create new faculty
- `GET /faculty/{id}` - Get faculty by ID
- `PUT /faculty/{id}` - Update faculty
- `DELETE /faculty/{id}` - Delete faculty

#### Notifications
- `GET /notifications` - Get all notifications
- `POST /notifications` - Create notification
- `GET /notifications/{id}` - Get notification by ID
- `PUT /notifications/{id}` - Update notification
- `DELETE /notifications/{id}` - Delete notification

#### Results
- `GET /results` - Get all results
- `POST /results` - Create result
- `GET /results/search?enrollment_no={no}` - Search results by enrollment

#### Timetables
- `GET /timetables` - Get all timetables
- `POST /timetables` - Create timetable
- `GET /timetables/weekly?program={program}&semester={sem}` - Get weekly schedule

#### Gallery
- `GET /gallery` - Get all gallery items
- `POST /gallery/upload` - Upload image
- `GET /gallery/featured` - Get featured images

## 🎨 Design Features

### Color Scheme
- **Primary:** Deep Blue (#1e3a8a) - Represents trust and professionalism
- **Secondary:** Saffron Orange (#f97316) - Reflects Indian heritage
- **Accent:** Green (#059669) - Symbolizes growth and education

### Typography
- **Headers:** Bold, clear fonts for readability
- **Body Text:** Clean, professional typography
- **Responsive:** Scales appropriately across devices

### Layout
- **Hero Section:** Engaging welcome message with call-to-action
- **Quick Access:** Easy navigation to important features
- **Program Showcase:** Detailed information about BA programs
- **Statistics:** College achievements and numbers
- **Footer:** Comprehensive links and contact information

## 🔧 Configuration

### Environment Variables
Create `.env` files in both frontend and backend directories:

**Backend (.env)**
```
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///college.db
```

**Frontend (.env)**
```
VITE_API_BASE_URL=http://localhost:5000/api
```

## 📱 Mobile Responsiveness

The website is fully responsive and optimized for:
- **Desktop:** Full-featured experience with all elements visible
- **Tablet:** Adapted layout with touch-friendly navigation
- **Mobile:** Collapsed navigation, stacked content, optimized images

## 🔒 Security Features

- **Authentication:** Secure admin login system
- **Session Management:** Proper session handling
- **File Upload Validation:** Restricted file types and sizes
- **CORS Configuration:** Controlled cross-origin access
- **Input Validation:** Server-side validation for all inputs

## 🚀 Deployment

### Development
Both frontend and backend run locally for development:
- Frontend: `npm run dev` (Port 5173)
- Backend: `python src/main.py` (Port 5000)

### Production
For production deployment, see `deployment-guide.md` for detailed instructions on:
- Building the React application
- Configuring Flask for production
- Setting up a web server (Nginx/Apache)
- Database configuration
- SSL certificate setup

## 📊 Sample Data

The application comes with pre-populated sample data:
- **5 Students** across different programs and semesters
- **6 Faculty Members** from various departments
- **5 Notifications** covering different categories
- **11 Timetable Entries** for different programs
- **6 Result Records** for sample students
- **4 Gallery Items** showcasing college infrastructure

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Government College of Gulabganj**
- **Address:** Government Higher Secondary School Campus, Gulabganj, District Vidisha, Madhya Pradesh - 464220
- **Phone:** +91 98264 58553
- **Email:** hegcgulvid@mp.gov.in

**Developer Contact:**
- **GitHub:** [@ajitameena94](https://github.com/ajitameena94)
- **Repository:** [GovtClgGulabgabj](https://github.com/ajitameena94/GovtClgGulabgabj)

## 🙏 Acknowledgments

- Government of Madhya Pradesh for supporting higher education
- Faculty and staff of Government College Gulabganj
- Open source community for the amazing tools and libraries
- Students and stakeholders for their valuable feedback

---

**Made with ❤️ for Government College of Gulabganj, Vidisha**

