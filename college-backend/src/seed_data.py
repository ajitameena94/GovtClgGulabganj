#!/usr/bin/env python3
"""
Seed script to populate the database with sample data for testing
"""
import os
import sys
from datetime import datetime, date

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.models.user import db
from src.models.college import Admin, Student, Faculty, Notification, Result, Timetable, Gallery
from src.main import app

def seed_database():
    with app.app_context():
        print("Seeding database with sample data...")
        
        # Create sample students
        students_data = [
            {
                'enrollment_no': 'GCG2024001',
                'name': 'Aarav Sharma',
                'email': 'aarav.sharma@student.gcg.edu.in',
                'phone': '9876543210',
                'program': 'BA History',
                'semester': 1,
                'year_of_admission': 2024
            },
            {
                'enrollment_no': 'GCG2024002',
                'name': 'Priya Patel',
                'email': 'priya.patel@student.gcg.edu.in',
                'phone': '9876543211',
                'program': 'BA Economics',
                'semester': 1,
                'year_of_admission': 2024
            },
            {
                'enrollment_no': 'GCG2023001',
                'name': 'Rohit Kumar',
                'email': 'rohit.kumar@student.gcg.edu.in',
                'phone': '9876543212',
                'program': 'BA Political Science',
                'semester': 3,
                'year_of_admission': 2023
            },
            {
                'enrollment_no': 'GCG2023002',
                'name': 'Sneha Gupta',
                'email': 'sneha.gupta@student.gcg.edu.in',
                'phone': '9876543213',
                'program': 'BA Sociology',
                'semester': 3,
                'year_of_admission': 2023
            },
            {
                'enrollment_no': 'GCG2022001',
                'name': 'Vikash Singh',
                'email': 'vikash.singh@student.gcg.edu.in',
                'phone': '9876543214',
                'program': 'BA Hindi Literature',
                'semester': 5,
                'year_of_admission': 2022
            }
        ]
        
        for student_data in students_data:
            existing_student = Student.query.filter_by(enrollment_no=student_data['enrollment_no']).first()
            if not existing_student:
                student = Student(**student_data)
                db.session.add(student)
        
        # Create sample faculty
        faculty_data = [
            {
                'employee_id': 'GCG001',
                'name': 'Dr. Rajesh Kumar Sharma',
                'email': 'rajesh.sharma@gcg.edu.in',
                'phone': '9876543220',
                'department': 'History',
                'designation': 'Principal',
                'qualification': 'Ph.D. in History',
                'experience': '25 years'
            },
            {
                'employee_id': 'GCG002',
                'name': 'Dr. Sunita Verma',
                'email': 'sunita.verma@gcg.edu.in',
                'phone': '9876543221',
                'department': 'Economics',
                'designation': 'Professor',
                'qualification': 'Ph.D. in Economics',
                'experience': '20 years'
            },
            {
                'employee_id': 'GCG003',
                'name': 'Prof. Anil Kumar Jain',
                'email': 'anil.jain@gcg.edu.in',
                'phone': '9876543222',
                'department': 'Political Science',
                'designation': 'Associate Professor',
                'qualification': 'M.A., Ph.D. in Political Science',
                'experience': '15 years'
            },
            {
                'employee_id': 'GCG004',
                'name': 'Dr. Meera Patel',
                'email': 'meera.patel@gcg.edu.in',
                'phone': '9876543223',
                'department': 'Sociology',
                'designation': 'Assistant Professor',
                'qualification': 'Ph.D. in Sociology',
                'experience': '12 years'
            },
            {
                'employee_id': 'GCG005',
                'name': 'Prof. Ramesh Gupta',
                'email': 'ramesh.gupta@gcg.edu.in',
                'phone': '9876543224',
                'department': 'Hindi Literature',
                'designation': 'Professor',
                'qualification': 'M.A., Ph.D. in Hindi Literature',
                'experience': '18 years'
            },
            {
                'employee_id': 'GCG006',
                'name': 'Dr. Priya Singh',
                'email': 'priya.singh@gcg.edu.in',
                'phone': '9876543225',
                'department': 'English Literature',
                'designation': 'Assistant Professor',
                'qualification': 'Ph.D. in English Literature',
                'experience': '10 years'
            }
        ]
        
        for faculty_info in faculty_data:
            existing_faculty = Faculty.query.filter_by(employee_id=faculty_info['employee_id']).first()
            if not existing_faculty:
                faculty = Faculty(**faculty_info)
                db.session.add(faculty)
        
        # Create sample notifications
        notifications_data = [
            {
                'title': 'Admission Open for Session 2024-25',
                'content': 'Applications are now open for BA programs in History, Economics, Sociology, Political Science, Hindi Literature, and English Literature. Last date for application is March 31, 2024.',
                'category': 'admission',
                'priority': 'high',
                'target_audience': 'all',
                'created_by': 1
            },
            {
                'title': 'Semester Examination Schedule Released',
                'content': 'The examination schedule for odd semester 2023-24 has been released. Students can check their exam dates on the college website.',
                'category': 'exam',
                'priority': 'normal',
                'target_audience': 'students',
                'created_by': 1
            },
            {
                'title': 'Annual Cultural Function - 2024',
                'content': 'The annual cultural function will be held on February 15, 2024. All students are invited to participate in various cultural activities.',
                'category': 'event',
                'priority': 'normal',
                'target_audience': 'all',
                'created_by': 1
            },
            {
                'title': 'Library Timing Update',
                'content': 'Library timing has been extended. New timings: Monday to Friday 8:00 AM to 6:00 PM, Saturday 8:00 AM to 2:00 PM.',
                'category': 'general',
                'priority': 'low',
                'target_audience': 'students',
                'created_by': 1
            },
            {
                'title': 'Faculty Development Program',
                'content': 'A faculty development program on modern teaching methodologies will be conducted from March 1-5, 2024.',
                'category': 'academic',
                'priority': 'normal',
                'target_audience': 'faculty',
                'created_by': 1
            }
        ]
        
        for notification_data in notifications_data:
            existing_notification = Notification.query.filter_by(title=notification_data['title']).first()
            if not existing_notification:
                notification = Notification(**notification_data)
                db.session.add(notification)
        
        # Create sample timetables
        timetables_data = [
            # BA History - Semester 1
            {'program': 'BA History', 'semester': 1, 'day_of_week': 'Monday', 'time_slot': '9:00-10:00', 'subject': 'Ancient Indian History', 'faculty_id': 1, 'room_no': 'Room 101'},
            {'program': 'BA History', 'semester': 1, 'day_of_week': 'Monday', 'time_slot': '10:00-11:00', 'subject': 'English', 'faculty_id': 6, 'room_no': 'Room 101'},
            {'program': 'BA History', 'semester': 1, 'day_of_week': 'Tuesday', 'time_slot': '9:00-10:00', 'subject': 'Medieval Indian History', 'faculty_id': 1, 'room_no': 'Room 101'},
            {'program': 'BA History', 'semester': 1, 'day_of_week': 'Tuesday', 'time_slot': '10:00-11:00', 'subject': 'Hindi', 'faculty_id': 5, 'room_no': 'Room 101'},
            
            # BA Economics - Semester 1
            {'program': 'BA Economics', 'semester': 1, 'day_of_week': 'Monday', 'time_slot': '11:00-12:00', 'subject': 'Microeconomics', 'faculty_id': 2, 'room_no': 'Room 102'},
            {'program': 'BA Economics', 'semester': 1, 'day_of_week': 'Monday', 'time_slot': '12:00-13:00', 'subject': 'Mathematics for Economics', 'faculty_id': 2, 'room_no': 'Room 102'},
            {'program': 'BA Economics', 'semester': 1, 'day_of_week': 'Tuesday', 'time_slot': '11:00-12:00', 'subject': 'Macroeconomics', 'faculty_id': 2, 'room_no': 'Room 102'},
            
            # BA Political Science - Semester 3
            {'program': 'BA Political Science', 'semester': 3, 'day_of_week': 'Wednesday', 'time_slot': '9:00-10:00', 'subject': 'Indian Government and Politics', 'faculty_id': 3, 'room_no': 'Room 103'},
            {'program': 'BA Political Science', 'semester': 3, 'day_of_week': 'Wednesday', 'time_slot': '10:00-11:00', 'subject': 'Comparative Politics', 'faculty_id': 3, 'room_no': 'Room 103'},
            
            # BA Sociology - Semester 3
            {'program': 'BA Sociology', 'semester': 3, 'day_of_week': 'Thursday', 'time_slot': '9:00-10:00', 'subject': 'Social Theory', 'faculty_id': 4, 'room_no': 'Room 104'},
            {'program': 'BA Sociology', 'semester': 3, 'day_of_week': 'Thursday', 'time_slot': '10:00-11:00', 'subject': 'Research Methods', 'faculty_id': 4, 'room_no': 'Room 104'},
        ]
        
        for timetable_data in timetables_data:
            existing_timetable = Timetable.query.filter_by(
                program=timetable_data['program'],
                semester=timetable_data['semester'],
                day_of_week=timetable_data['day_of_week'],
                time_slot=timetable_data['time_slot']
            ).first()
            if not existing_timetable:
                timetable = Timetable(**timetable_data)
                db.session.add(timetable)
        
        # Create sample results
        results_data = [
            # Results for Rohit Kumar (GCG2023001) - Semester 1
            {'student_id': 3, 'semester': 1, 'subject': 'Ancient Indian History', 'marks_obtained': 85, 'total_marks': 100, 'grade': 'A', 'exam_type': 'Semester', 'exam_year': 2023},
            {'student_id': 3, 'semester': 1, 'subject': 'Medieval Indian History', 'marks_obtained': 78, 'total_marks': 100, 'grade': 'B+', 'exam_type': 'Semester', 'exam_year': 2023},
            {'student_id': 3, 'semester': 1, 'subject': 'English', 'marks_obtained': 72, 'total_marks': 100, 'grade': 'B+', 'exam_type': 'Semester', 'exam_year': 2023},
            
            # Results for Sneha Gupta (GCG2023002) - Semester 1
            {'student_id': 4, 'semester': 1, 'subject': 'Introduction to Sociology', 'marks_obtained': 88, 'total_marks': 100, 'grade': 'A', 'exam_type': 'Semester', 'exam_year': 2023},
            {'student_id': 4, 'semester': 1, 'subject': 'Social Psychology', 'marks_obtained': 82, 'total_marks': 100, 'grade': 'A', 'exam_type': 'Semester', 'exam_year': 2023},
            {'student_id': 4, 'semester': 1, 'subject': 'English', 'marks_obtained': 75, 'total_marks': 100, 'grade': 'B+', 'exam_type': 'Semester', 'exam_year': 2023},
        ]
        
        for result_data in results_data:
            existing_result = Result.query.filter_by(
                student_id=result_data['student_id'],
                semester=result_data['semester'],
                subject=result_data['subject'],
                exam_year=result_data['exam_year']
            ).first()
            if not existing_result:
                result = Result(**result_data)
                db.session.add(result)
        
        # Create sample gallery items
        gallery_data = [
            {
                'title': 'College Main Building',
                'description': 'The main academic building of Government College Gulabganj',
                'image_url': '/uploads/gallery/college_building.jpg',
                'category': 'infrastructure',
                'is_featured': True,
                'uploaded_by': 1
            },
            {
                'title': 'Annual Function 2023',
                'description': 'Students performing during the annual cultural function',
                'image_url': '/uploads/gallery/annual_function_2023.jpg',
                'category': 'events',
                'event_date': date(2023, 12, 15),
                'is_featured': True,
                'uploaded_by': 1
            },
            {
                'title': 'Library Reading Hall',
                'description': 'Students studying in the college library',
                'image_url': '/uploads/gallery/library.jpg',
                'category': 'infrastructure',
                'is_featured': True,
                'uploaded_by': 1
            },
            {
                'title': 'Sports Day 2023',
                'description': 'Annual sports competition among students',
                'image_url': '/uploads/gallery/sports_day.jpg',
                'category': 'activities',
                'event_date': date(2023, 11, 20),
                'is_featured': False,
                'uploaded_by': 1
            }
        ]
        
        for gallery_item in gallery_data:
            existing_item = Gallery.query.filter_by(title=gallery_item['title']).first()
            if not existing_item:
                gallery = Gallery(**gallery_item)
                db.session.add(gallery)
        
        # Commit all changes
        db.session.commit()
        print("Database seeded successfully!")
        
        # Print summary
        print(f"Created {len(students_data)} students")
        print(f"Created {len(faculty_data)} faculty members")
        print(f"Created {len(notifications_data)} notifications")
        print(f"Created {len(timetables_data)} timetable entries")
        print(f"Created {len(results_data)} result records")
        print(f"Created {len(gallery_data)} gallery items")

if __name__ == '__main__':
    seed_database()

