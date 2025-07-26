import os
import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from src.models.user import db
from src.models.college import Admin
from src.routes.user import user_bp
from src.routes.auth import auth_bp
from src.routes.students import students_bp
from src.routes.faculty import faculty_bp
from src.routes.results import results_bp
from src.routes.timetables import timetables_bp
from src.routes.notifications import notifications_bp
from src.routes.gallery import gallery_bp
from src.routes.facilities import facilities_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this in production!
jwt = JWTManager(app)

# Enable CORS for all routes
CORS(app, origins=["http://localhost:5173", "https://ajitameena94.github.io"], supports_credentials=True)

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(students_bp, url_prefix='/api')
app.register_blueprint(faculty_bp, url_prefix='/api')
app.register_blueprint(results_bp, url_prefix='/api')
app.register_blueprint(timetables_bp, url_prefix='/api')
app.register_blueprint(notifications_bp, url_prefix='/api')
app.register_blueprint(gallery_bp, url_prefix='/api')
app.register_blueprint(facilities_bp, url_prefix='/api')

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://college_db_aib3_user:lNs5Olyvg9o7RmQM1vGJ9lpQvNak4B4o@dpg-d20rk7mmcj7s73e38g40-a/college_db_aib3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

db.init_app(app)
with app.app_context():
    db.create_all()
    
    # Create default admin if not exists
    admin = Admin.query.filter_by(username='admin').first()
    if not admin:
        admin = Admin(username='admin', email='admin@gulabganjcollege.edu.in')
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print("Default admin created: username=admin, password=admin123")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
