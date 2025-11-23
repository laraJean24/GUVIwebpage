# User Management System - Setup Guide

## Project Overview
A complete user authentication system with registration, login, and profile management using HTML, CSS, JavaScript, PHP, MySQL, and Redis.

## Tech Stack
- **Frontend**: HTML5, CSS3, Bootstrap 5, jQuery with AJAX
- **Backend**: PHP (with Prepared Statements)
- **Database**: MySQL
- **Session Management**: Redis + Browser LocalStorage
- **Architecture**: Separated Frontend/Backend with AJAX communication

## Folder Structure
```
Guvi_project/
├── index.html              # Home page
├── register.html           # Registration page
├── login.html              # Login page
├── profile.html            # User profile page
├── database-schema.sql     # MySQL database schema
├── css/
│   └── styles.css          # Custom CSS with Bootstrap
├── js/
│   ├── register.js         # Registration form handling with AJAX
│   ├── login.js            # Login form handling with AJAX
│   └── profile.js          # Profile page handling with AJAX
├── php/
│   ├── register.php        # Registration endpoint (prepared statements)
│   ├── login.php           # Login endpoint (Redis session)
│   ├── profile.php         # Profile fetch endpoint
│   ├── update-profile.php  # Profile update endpoint (prepared statements)
│   └── logout.php          # Logout endpoint (Redis session deletion)
└── config/
    ├── db-config.php       # MySQL database configuration
    └── redis-config.php    # Redis session configuration
```

## Prerequisites
- PHP 7.4+
- MySQL 5.7+
- Redis Server
- Web Server (Apache/Nginx)
- PHP Extensions: mysqli, redis

## Installation Steps

### 1. Database Setup
```bash
# Connect to MySQL
mysql -u root -p

# Execute the schema
SOURCE /path/to/database-schema.sql;
```

### 2. Redis Setup
```bash
# Windows (if using Windows)
# Download Redis from https://github.com/microsoftarchive/redis/releases
# Extract and run redis-server.exe

# Linux
sudo apt-get install redis-server
sudo service redis-server start

# macOS
brew install redis
brew services start redis
```

### 3. Web Server Configuration
Copy the project folder to your web root:
- **Apache**: C:\xampp\htdocs\ (Windows) or /var/www/html/ (Linux)
- **Nginx**: /usr/share/nginx/html/ (Linux)

### 4. Database Connection
Edit `config/db-config.php` and update:
```php
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'user_management_db');
```

### 5. Redis Connection
Edit `config/redis-config.php` and verify:
```php
define('REDIS_HOST', 'localhost');
define('REDIS_PORT', 6379);
```

## Usage

### User Registration
1. Navigate to `http://localhost/Guvi_project/register.html`
2. Fill in the registration form:
   - First Name
   - Last Name
   - Email
   - Password (min 6 characters)
   - Confirm Password
3. Click "Register" button
4. Success message will redirect to login page

### User Login
1. Navigate to `http://localhost/Guvi_project/login.html`
2. Enter email and password
3. Click "Login" button
4. Session token stored in browser LocalStorage
5. Redirected to profile page

### Profile Management
1. On profile page, user sees:
   - Read-only: First Name, Last Name, Email
   - Editable: Age, DOB, Contact, Address, City, State, Zip Code
2. Fill in additional details
3. Click "Save Changes" to update
4. Click "Logout" to end session

## Key Features Implemented

### ✅ All Requirements Met:

1. **Separate File Organization**
   - HTML, CSS, JS, PHP in separate files
   - No code mixed in single files

2. **jQuery AJAX Only**
   - All form submissions use AJAX
   - No traditional form submission
   - Asynchronous communication with backend

3. **Bootstrap Responsive Design**
   - Forms designed with Bootstrap 5
   - Mobile-friendly layout
   - Responsive grid system

4. **MySQL with Prepared Statements**
   - All SQL uses MySQLi prepared statements
   - NO vulnerable SQL concatenation
   - Parameter binding for security

5. **Browser LocalStorage for Session**
   - Session token stored in browser localStorage
   - NO PHP session usage
   - Token passed to backend for validation

6. **Redis for Backend Session**
   - Session data stored in Redis
   - Fast session retrieval
   - Automatic expiry management
   - 24-hour session timeout

## Security Features

1. **Password Security**
   - Bcrypt hashing (PASSWORD_BCRYPT)
   - Salt generation automatic

2. **Session Management**
   - Unique session tokens (random_bytes)
   - Redis expiry for inactive sessions
   - Token validation on every request

3. **Database Security**
   - Prepared statements prevent SQL injection
   - Parameter binding
   - Type-safe queries

4. **Frontend Validation**
   - Email format validation
   - Password strength check
   - Field requirement validation

5. **Backend Validation**
   - Duplicate email prevention
   - Password verification
   - Session token validation

## API Endpoints

### POST /php/register.php
**Request:**
```json
{
    "firstName": "John",
    "lastName": "Doe",
    "email": "john@example.com",
    "password": "password123"
}
```
**Response:**
```json
{
    "success": true,
    "message": "Registration successful! Please login."
}
```

### POST /php/login.php
**Request:**
```json
{
    "email": "john@example.com",
    "password": "password123"
}
```
**Response:**
```json
{
    "success": true,
    "message": "Login successful!",
    "token": "session_token_here"
}
```

### POST /php/profile.php
**Request:**
```json
{
    "sessionToken": "session_token_here"
}
```
**Response:**
```json
{
    "success": true,
    "data": {
        "id": 1,
        "firstName": "John",
        "lastName": "Doe",
        "email": "john@example.com",
        "age": 25,
        "dob": "1998-01-15",
        "contact": "1234567890",
        "address": "123 Street",
        "city": "City",
        "state": "State",
        "zipcode": "12345"
    }
}
```

### POST /php/update-profile.php
**Request:**
```json
{
    "sessionToken": "session_token_here",
    "age": 25,
    "dob": "1998-01-15",
    "contact": "1234567890",
    "address": "123 Street",
    "city": "City",
    "state": "State",
    "zipcode": "12345"
}
```
**Response:**
```json
{
    "success": true,
    "message": "Profile updated successfully"
}
```

### POST /php/logout.php
**Request:**
```json
{
    "sessionToken": "session_token_here"
}
```
**Response:**
```json
{
    "success": true,
    "message": "Logged out successfully"
}
```

## Testing

### Sample Login Credentials
- **Email**: test@example.com
- **Password**: password123

### Test Flow
1. Start at `http://localhost/Guvi_project/index.html`
2. Create a new account via registration page
3. Login with created credentials
4. Update profile with additional details
5. Logout and verify session is cleared

## Troubleshooting

### Database Connection Error
- Verify MySQL is running
- Check credentials in `config/db-config.php`
- Ensure database exists: `user_management_db`

### Redis Connection Error
- Verify Redis server is running
- Check host and port in `config/redis-config.php`
- On Windows, ensure redis-server.exe is running

### Session Errors
- Clear browser localStorage: DevTools > Application > Storage
- Check Redis connection
- Verify session token in localStorage

### AJAX Errors
- Check browser console for errors (F12)
- Verify PHP files exist and are readable
- Check server error logs
- Ensure CORS headers in PHP files

## Performance Optimization

1. **Database Indexes**
   - Email index for quick lookups
   - Composite indexes for common queries

2. **Redis Caching**
   - Session data cached in Redis
   - Fast retrieval without DB hits

3. **Lazy Loading**
   - Profile data loaded on demand
   - Spinner shown during loading

4. **Minification** (Optional)
   - Minify CSS and JS for production
   - Compress images in assets

## Browser Support
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Notes
- All passwords stored with bcrypt hashing
- Session expires after 24 hours of inactivity
- Email must be unique per user
- Profile fields (age, dob, contact, address, etc.) are optional
- Contact field accepts phone numbers
- Age validation: 1-120 years

## Submission Checklist
- [x] HTML, JS, CSS, PHP in separate files
- [x] jQuery AJAX only for backend communication
- [x] Bootstrap form design
- [x] MySQL with prepared statements
- [x] Browser localStorage for client-side session
- [x] Redis for server-side session storage
- [x] Registration → Login → Profile flow
- [x] User data update capability
- [x] Logout functionality
- [x] Responsive design

## Support & Contact
For issues or questions, refer to the code comments in each file.
