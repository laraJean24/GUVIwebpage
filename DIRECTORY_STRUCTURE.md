# Complete Project Directory Structure

```
e:\Guvi_project
│
├── 📄 index.html (Home page - HTML only)
├── 📄 register.html (Registration page - HTML only)
├── 📄 login.html (Login page - HTML only)
├── 📄 profile.html (Profile page - HTML only)
│
├── 📄 database-schema.sql (MySQL schema)
├── 📄 docker-compose.yml (Docker containers setup)
├── 📄 .htaccess (Apache configuration)
│
├── 📚 README.md (Complete documentation)
├── 📚 QUICKSTART.md (Setup guide for all platforms)
├── 📚 PROJECT_STRUCTURE.md (Detailed structure documentation)
├── 📚 SUBMISSION_SUMMARY.md (Requirements checklist)
├── 📚 VERIFICATION_CHECKLIST.md (Pre-submission verification)
│
├── 📁 css/
│   └── 🎨 styles.css (All CSS styling - Bootstrap + Custom)
│
├── 📁 js/
│   ├── 📜 register.js (Registration AJAX handler)
│   ├── 📜 login.js (Login AJAX handler)
│   └── 📜 profile.js (Profile AJAX handler)
│
├── 📁 php/
│   ├── 🔒 register.php (Registration endpoint - Prepared Statements)
│   ├── 🔒 login.php (Login endpoint - Redis Session)
│   ├── 🔒 profile.php (Profile fetch endpoint)
│   ├── 🔒 update-profile.php (Profile update endpoint - Prepared Statements)
│   └── 🔒 logout.php (Logout endpoint - Redis deletion)
│
├── 📁 config/
│   ├── ⚙️ db-config.php (MySQL configuration)
│   └── ⚙️ redis-config.php (Redis session configuration)
│
└── 📁 assets/ (Optional - for future images/files)
```

## File Count Summary

| Category | Count | Details |
|----------|-------|---------|
| HTML Files | 4 | index.html, register.html, login.html, profile.html |
| CSS Files | 1 | styles.css (All styling) |
| JavaScript Files | 3 | register.js, login.js, profile.js |
| PHP Files | 5 | register.php, login.php, profile.php, update-profile.php, logout.php |
| Config Files | 2 | db-config.php, redis-config.php |
| Setup Files | 4 | database-schema.sql, docker-compose.yml, .htaccess, assets/ |
| Documentation | 5 | README.md, QUICKSTART.md, PROJECT_STRUCTURE.md, SUBMISSION_SUMMARY.md, VERIFICATION_CHECKLIST.md |
| **TOTAL** | **24** | **Complete project** |

## Organization Overview

### Frontend (Presentation Layer)
```
index.html ─────────────┐
register.html ────┐     │
login.html ───────┼─ Uses ─ css/styles.css (Bootstrap + Custom)
profile.html ─────┤         js/register.js (AJAX)
                  └─────── js/login.js (AJAX)
                          js/profile.js (AJAX)
```

### Backend (Application Layer)
```
js/register.js ────┐
js/login.js ───────┼─ Makes AJAX requests to ─ php/register.php
js/profile.js ─────┤                           php/login.php
                   └─────────────────────── php/profile.php
                                            php/update-profile.php
                                            php/logout.php
```

### Data Layer
```
php/register.php ──┐
php/login.php ─────┼─ Uses prepared statements ─ MySQL Database
php/profile.php ───┤   (with bind_param())      (user_management_db)
php/update-profile.php│
php/logout.php ────┴─ Uses Redis ─────────────── Redis Server
                                                  (Session Storage)
```

### Configuration
```
config/db-config.php ──────────── MySQL credentials
config/redis-config.php ───────── Redis configuration
```

## Technology Stack Overview

```
Browser (Client)
    │
    ├─── HTML5 (index.html, register.html, login.html, profile.html)
    ├─── CSS3 (css/styles.css + Bootstrap 5)
    ├─── jQuery (js/register.js, js/login.js, js/profile.js)
    └─── AJAX (POST requests to PHP endpoints)
         │
         └──────────────────────────────────────────┐
                                                    │
                    Apache/Nginx Web Server         │
                                                    ▼
                    PHP 8.0+ (Application Server)
                    │
                    ├─── php/register.php (Prepared Statements)
                    ├─── php/login.php (Session Management)
                    ├─── php/profile.php (Data Retrieval)
                    ├─── php/update-profile.php (Data Update)
                    └─── php/logout.php (Session Cleanup)
                         │
                         ├─────────────────┬──────────────────┐
                         │                 │                  │
                         ▼                 ▼                  ▼
                    MySQL Database    Redis Server        File System
                    (Users Data)      (Sessions)          (Logs)
```

## Request/Response Flow

### Registration Flow
```
register.html
    │
    │ (User enters data)
    │ e.preventDefault()
    │
    ▼
register.js
    │
    │ Validation (frontend)
    │ $.ajax POST
    │
    ▼
register.php
    │
    │ Validation (backend)
    │ Check duplicate email (Prepared Statement)
    │ Hash password (bcrypt)
    │ Insert user (Prepared Statement)
    │
    ▼
MySQL Database
    │
    │ Success
    │
    ▼
register.php returns JSON
    │
    ▼
register.js receives response
    │
    │ Show success message
    │ Redirect to login.html
    │
    ▼
login.html
```

### Login Flow
```
login.html
    │
    │ (User enters credentials)
    │ e.preventDefault()
    │
    ▼
login.js
    │
    │ Validation (frontend)
    │ $.ajax POST
    │
    ▼
login.php
    │
    │ Get user (Prepared Statement)
    │ Verify password (bcrypt)
    │ Generate session token (random_bytes)
    │
    ▼
Redis Server
    │
    │ Store session data
    │
    ▼
login.php returns JSON + token
    │
    ▼
login.js receives response
    │
    │ Store token in localStorage
    │ Redirect to profile.html
    │
    ▼
profile.html
```

### Profile Flow
```
profile.html (loads)
    │
    │ Check localStorage for token
    │ $.ajax POST with token
    │
    ▼
profile.js
    │
    │ Validation (token exists)
    │ $.ajax POST
    │
    ▼
profile.php
    │
    │ Get session from Redis
    │ Get user from MySQL (Prepared Statement)
    │ Extend session expiry
    │
    ▼
profile.js receives response
    │
    │ Populate form fields
    │ Display profile
    │
    ▼
User views/updates profile
    │
    │ Submit form
    │ $.ajax POST
    │
    ▼
update-profile.php
    │
    │ Validate session (Redis)
    │ Validate input
    │ Update user (Prepared Statement)
    │
    ▼
MySQL Database
    │
    │ Update profile
    │
    ▼
update-profile.php returns JSON
    │
    ▼
profile.js shows success
    │
    │ User clicks Logout
    │ $.ajax POST
    │
    ▼
logout.php
    │
    │ Delete session from Redis
    │
    ▼
logout.php returns JSON
    │
    ▼
profile.js clears localStorage
    │
    │ Redirect to login.html
    │
    ▼
login.html
```

## Security Layers

### Layer 1: Frontend Validation
```
register.js
├─ Check empty fields
├─ Validate email format
├─ Check password strength
└─ Confirm password match
```

### Layer 2: AJAX Communication
```
All AJAX requests
├─ POST method only
├─ JSON data format
├─ CORS headers
└─ No sensitive data in URL
```

### Layer 3: Backend Validation & Processing
```
register.php, login.php, profile.php, etc.
├─ Prepared Statements (SQL Injection Prevention)
├─ Parameter Binding
├─ Input Sanitization
├─ Password Hashing (bcrypt)
├─ Session Token Validation
└─ Error Handling
```

### Layer 4: Session Management
```
Browser (Client)
├─ localStorage - Session Token
└─ HTTPS (recommended)

Server (Backend)
├─ Redis - Session Data
├─ 24-hour Expiry
├─ Token Validation
└─ Secure Token Generation
```

### Layer 5: Database Security
```
MySQL Database
├─ Prepared Statements (All queries)
├─ Parameter Binding
├─ Password Hashing
├─ User Isolation
└─ Access Control
```

## Setup Components

### docker-compose.yml Services
```
MySQL Service
├─ Image: mysql:8.0
├─ Port: 3306
├─ Database: user_management_db
└─ Volumes: Database persistence

Redis Service
├─ Image: redis:7-alpine
├─ Port: 6379
├─ Volumes: Data persistence
└─ Health Check: redis-cli ping

PHP Service
├─ Image: php:8.0-apache
├─ Port: 80
├─ Extensions: mysqli, redis
└─ Volumes: Project files
```

## Documentation Files Organization

```
README.md
├─ Overview
├─ Setup Instructions (Windows/Linux/macOS)
├─ Usage Guide
├─ API Documentation
├─ Troubleshooting
└─ Security Features

QUICKSTART.md
├─ Docker Setup
├─ Manual Setup (all platforms)
├─ Common Issues & Solutions
├─ Testing Procedures
├─ Performance Tuning
└─ Security Hardening

PROJECT_STRUCTURE.md
├─ File Descriptions
├─ Data Flow Diagrams
├─ Technology Stack
├─ Code Organization
└─ Standards & Best Practices

SUBMISSION_SUMMARY.md
├─ Requirements Checklist
├─ File Summary
├─ Security Features
├─ Key Features List
└─ Compliance Summary

VERIFICATION_CHECKLIST.md
├─ File Organization Check
├─ AJAX Implementation Check
├─ Bootstrap Design Check
├─ Security Check
└─ Testing Verification
```

## Key Features by Component

### Registration
- ✅ Separate HTML, CSS, JS, PHP
- ✅ jQuery AJAX (no form submission)
- ✅ Bootstrap responsive form
- ✅ Prepared statement query
- ✅ Email validation
- ✅ Password hashing (bcrypt)
- ✅ Duplicate email prevention
- ✅ Proper error handling

### Login
- ✅ Separate files
- ✅ jQuery AJAX only
- ✅ Bootstrap form design
- ✅ Prepared statement query
- ✅ Password verification
- ✅ Redis session creation
- ✅ LocalStorage token storage
- ✅ Session token generation (random_bytes)

### Profile
- ✅ Separate files
- ✅ jQuery AJAX for all operations
- ✅ Bootstrap responsive layout
- ✅ Prepared statements
- ✅ Session validation
- ✅ Data persistence
- ✅ Update functionality
- ✅ Logout with cleanup

## Compliance Matrix

| Requirement | HTML | CSS | JS | PHP | Config | Status |
|-------------|------|-----|----|----|--------|--------|
| Separate Files | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ PASS |
| No Mixed Code | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ PASS |
| AJAX Only | - | - | ✅ | - | - | ✅ PASS |
| Bootstrap | - | ✅ | - | - | - | ✅ PASS |
| Prepared Statements | - | - | - | ✅ | - | ✅ PASS |
| LocalStorage | - | - | ✅ | - | - | ✅ PASS |
| Redis Sessions | - | - | - | ✅ | ✅ | ✅ PASS |
| Full Flow | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ PASS |

**Overall Status: 🎉 ALL REQUIREMENTS MET - READY FOR SUBMISSION 🎉**

---

## Quick Reference

### Files to Never Edit Together
- ❌ Don't mix HTML with CSS
- ❌ Don't mix HTML with JS
- ❌ Don't mix HTML with PHP
- ❌ Don't mix CSS with JS
- ❌ Don't mix CSS with PHP
- ❌ Don't mix JS with PHP

### Files to Always Keep Separate
- ✅ Keep HTML files separate (index.html, register.html, login.html, profile.html)
- ✅ Keep CSS in single file (css/styles.css)
- ✅ Keep JS files separate by functionality (register.js, login.js, profile.js)
- ✅ Keep PHP files separate by endpoint (register.php, login.php, profile.php, update-profile.php, logout.php)
- ✅ Keep config in separate files (db-config.php, redis-config.php)

### Commands to Remember

**Start Docker:**
```bash
docker-compose up -d
```

**Stop Docker:**
```bash
docker-compose down
```

**Access Application:**
```
http://localhost/Guvi_project/index.html
```

**Test Credentials:**
```
Email: test@example.com
Password: password123
```

---

**Project Status: ✅ COMPLETE & READY FOR SUBMISSION**
