# Deployment Guide - Government College Gulabganj Website

This guide provides step-by-step instructions for deploying the college website to production.

## 🚀 Deployment Options

### Option 1: GitHub Pages (Frontend Only)
For static frontend deployment with mock data.

### Option 2: Heroku (Full Stack)
For complete application with backend functionality.

### Option 3: VPS/Cloud Server
For full control and custom configuration.

## 📋 Pre-deployment Checklist

- [ ] All tests passing
- [ ] Environment variables configured
- [ ] Database migrations ready
- [ ] Static files optimized
- [ ] Security configurations in place
- [ ] Domain name configured (if applicable)

## 🔧 Option 1: GitHub Pages Deployment

### Step 1: Prepare Frontend for Static Deployment
```bash
cd college-frontend
npm run build
```

### Step 2: Configure GitHub Pages
1. Push code to GitHub repository
2. Go to repository Settings → Pages
3. Select source: Deploy from a branch
4. Choose branch: main
5. Select folder: /docs or /root
6. Copy built files to selected folder

### Step 3: Update API URLs
For static deployment, update frontend to use mock data or external APIs.

## 🚀 Option 2: Heroku Deployment

### Step 1: Prepare Backend for Heroku
Create `Procfile` in backend directory:
```
web: python src/main.py
```

Create `runtime.txt`:
```
python-3.11.0
```

Update `requirements.txt`:
```bash
cd college-backend
pip freeze > requirements.txt
```

### Step 2: Configure Flask for Production
Update `src/main.py`:
```python
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

### Step 3: Deploy Backend to Heroku
```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-college-backend

# Set environment variables
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-production-secret-key

# Deploy
git add .
git commit -m "Prepare for Heroku deployment"
git push heroku main
```

### Step 4: Deploy Frontend
```bash
cd college-frontend

# Update API base URL in .env
VITE_API_BASE_URL=https://your-college-backend.herokuapp.com/api

# Build for production
npm run build

# Deploy to Netlify, Vercel, or GitHub Pages
```

## 🖥️ Option 3: VPS/Cloud Server Deployment

### Step 1: Server Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install required software
sudo apt install python3 python3-pip nodejs npm nginx -y

# Install PM2 for process management
sudo npm install -g pm2
```

### Step 2: Deploy Backend
```bash
# Clone repository
git clone https://github.com/ajitameena94/GovtClgGulabgabj.git
cd GovtClgGulabgabj/college-backend

# Setup Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Initialize database
python src/seed_data.py

# Start with PM2
pm2 start src/main.py --name college-backend --interpreter python3
pm2 save
pm2 startup
```

### Step 3: Deploy Frontend
```bash
cd ../college-frontend

# Install dependencies
npm install

# Build for production
npm run build

# Copy to web server directory
sudo cp -r dist/* /var/www/html/
```

### Step 4: Configure Nginx
Create `/etc/nginx/sites-available/college-website`:
```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;
    
    # Frontend
    location / {
        root /var/www/html;
        index index.html;
        try_files $uri $uri/ /index.html;
    }
    
    # Backend API
    location /api {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Static files
    location /uploads {
        alias /path/to/college-backend/src/static/uploads;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/college-website /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## 🔒 SSL Certificate Setup

### Using Let's Encrypt (Certbot)
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtain certificate
sudo certbot --nginx -d your-domain.com -d www.your-domain.com

# Auto-renewal
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

## 🗄️ Database Configuration

### Production Database Setup
For production, consider using PostgreSQL instead of SQLite:

```bash
# Install PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Create database and user
sudo -u postgres psql
CREATE DATABASE college_db;
CREATE USER college_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE college_db TO college_user;
\q
```

Update Flask configuration:
```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///college.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## 📊 Monitoring and Maintenance

### Log Management
```bash
# View PM2 logs
pm2 logs college-backend

# View Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

### Backup Strategy
```bash
# Database backup script
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
pg_dump college_db > /backups/college_db_$DATE.sql

# Keep only last 7 days of backups
find /backups -name "college_db_*.sql" -mtime +7 -delete
```

### Update Process
```bash
# Backend updates
cd college-backend
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
pm2 restart college-backend

# Frontend updates
cd ../college-frontend
git pull origin main
npm install
npm run build
sudo cp -r dist/* /var/www/html/
```

## 🔧 Environment Variables

### Production Environment Variables
Create `.env` file in backend:
```bash
FLASK_ENV=production
SECRET_KEY=your-very-secure-secret-key
DATABASE_URL=postgresql://college_user:secure_password@localhost/college_db
UPLOAD_FOLDER=/var/www/uploads
MAX_CONTENT_LENGTH=16777216
```

### Frontend Environment Variables
Create `.env.production` in frontend:
```bash
VITE_API_BASE_URL=https://your-domain.com/api
VITE_APP_TITLE=Government College of Gulabganj
```

## 🚨 Troubleshooting

### Common Issues

1. **CORS Errors**
   - Ensure CORS is properly configured in Flask
   - Check that frontend URL is allowed in CORS settings

2. **File Upload Issues**
   - Verify upload directory permissions
   - Check file size limits
   - Ensure proper file type validation

3. **Database Connection Issues**
   - Verify database credentials
   - Check database server status
   - Ensure proper database URL format

4. **Static Files Not Loading**
   - Check Nginx configuration
   - Verify file permissions
   - Ensure correct paths in configuration

### Performance Optimization

1. **Frontend Optimization**
   ```bash
   # Enable gzip compression in Nginx
   gzip on;
   gzip_types text/css application/javascript application/json image/svg+xml;
   ```

2. **Backend Optimization**
   ```python
   # Add caching headers
   from flask import make_response
   
   @app.after_request
   def after_request(response):
       response.headers['Cache-Control'] = 'public, max-age=300'
       return response
   ```

3. **Database Optimization**
   - Add database indexes for frequently queried fields
   - Use connection pooling
   - Implement query optimization

## 📈 Scaling Considerations

### Load Balancing
For high traffic, consider:
- Multiple backend instances
- Load balancer (Nginx, HAProxy)
- CDN for static assets
- Database read replicas

### Monitoring
Set up monitoring with:
- Application performance monitoring (APM)
- Server monitoring (CPU, memory, disk)
- Database monitoring
- Log aggregation

## 🔐 Security Checklist

- [ ] HTTPS enabled with valid SSL certificate
- [ ] Strong passwords and secret keys
- [ ] Regular security updates
- [ ] File upload restrictions
- [ ] Input validation and sanitization
- [ ] Rate limiting implemented
- [ ] Backup and recovery plan
- [ ] Access logs monitoring

## 📞 Support

For deployment issues or questions:
- Check the main README.md file
- Review application logs
- Contact the development team
- Submit issues on GitHub repository

---

**Happy Deploying! 🚀**

