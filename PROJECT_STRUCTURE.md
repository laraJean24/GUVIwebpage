# Project Structure Documentation

## Complete Folder Layout

```
Guvi_project/
│
├── index.html                    # Home/Landing page
├── login.html                    # Login form page
├── register.html                 # Registration form page
├── profile.html                  # User profile page
│
├── database-schema.sql           # MySQL database schema and setup
├── docker-compose.yml            # Docker setup for MySQL, Redis, PHP
├── .htaccess                     # Apache configuration
│
├── README.md                     # Complete documentation
├── QUICKSTART.md                 # Quick start guide for different platforms
│
├── css/
│   └── styles.css                # All CSS styling (Bootstrap + custom)
│
├── js/
│   ├── register.js               # Registration AJAX handler
│   ├── login.js                  # Login AJAX handler
│   └── profile.js                # Profile page AJAX handler
│
├── php/
│   ├── register.php              # Registration endpoint
│   ├── login.php                 # Login endpoint with Redis
│   ├── profile.php               # Profile fetch endpoint
│   ├── update-profile.php        # Profile update endpoint
│   └── logout.php                # Logout endpoint
│
├── config/
│   ├── db-config.php             # MySQL configuration
│   └── redis-config.php          # Redis session configuration
│
└── assets/                       # (Optional) For future images/files
```

## File Descriptions

### Frontend Files

#### `index.html` (Home Page)
- Welcome page with navigation
- Links to register and login pages
- Bootstrap styled card layout

#### `register.html` (Registration Page)
- Registration form with fields:
  - First Name, Last Name, Email, Password, Confirm Password
- Form validation
- Link to login page

#### `login.html` (Login Page)
- Login form with:
  - Email, Password fields
- Form validation
- Link to register page

#### `profile.html` (Profile Page)
- Displays user information
- Read-only fields: First Name, Last Name, Email
- Editable fields: Age, DOB, Contact, Address, City, State, Zipcode
- Logout button
- Update profile form

### CSS Files

#### `css/styles.css`
- Bootstrap 5 integration
- Custom styling for:
  - Cards and containers
  - Forms and inputs
  - Buttons with hover effects
  - Alerts and notifications
  - Navbar
  - Responsive design
  - Accessibility features

### JavaScript Files

#### `js/register.js`
- AJAX form submission for registration
- Client-side validation:
  - Email format check
  - Password strength
  - Password confirmation
- Error/Success message display
- Redirect on success

#### `js/login.js`
- AJAX form submission for login
- Form validation
- Store session token in localStorage
- Redirect to profile on success
- Error handling

#### `js/profile.js`
- Load user profile on page load
- Check login status
- Display user data
- Handle profile update via AJAX
- Logout functionality
- Session token validation

### PHP Backend Files

#### `php/register.php`
- Receives POST data from register.js
- Validation:
  - Email format
  - Password strength
  - Required fields
  - Duplicate email check (prepared statement)
- Password hashing with bcrypt
- Insert user data (prepared statement)
- JSON response

#### `php/login.php`
- Receives POST data from login.js
- Validate email and password
- Fetch user from MySQL (prepared statement)
- Password verification with bcrypt
- Generate session token
- Store session in Redis
- Return token to frontend

#### `php/profile.php`
- Receives session token from profile.js
- Validate session from Redis
- Fetch user data from MySQL (prepared statement)
- Return user profile data
- Extend session expiry in Redis

#### `php/update-profile.php`
- Receives session token and profile data
- Validate session
- Update user profile (prepared statement)
- Return success/error message

#### `php/logout.php`
- Receives session token
- Delete session from Redis
- Clear session token

### Configuration Files

#### `config/db-config.php`
- MySQL connection settings
- Database credentials
- Connection setup
- Error handling
- closeConnection() function

#### `config/redis-config.php`
- Redis connection class
- Session management methods:
  - setSession() - Store session
  - getSession() - Retrieve session
  - deleteSession() - Remove session
  - extendSession() - Refresh timeout
  - sessionExists() - Check validity
- Error handling

### Setup Files

#### `database-schema.sql`
- Create `user_management_db` database
- Create `users` table with columns:
  - id (PRIMARY KEY)
  - firstName, lastName, email, password
  - age, dob, contact, address, city, state, zipcode
  - createdAt, updatedAt
- Create indexes for performance
- Sample test user data

#### `docker-compose.yml`
- MySQL 8.0 service
- Redis 7 service
- PHP 8.0-Apache service
- Volume mappings
- Network configuration
- Health checks

#### `.htaccess`
- Apache configuration
- Enable mod_rewrite
- CORS headers
- Deny access to sensitive files
- Output compression
- Caching headers

#### `README.md`
- Complete project documentation
- Setup instructions for all OS
- Usage guide
- API endpoint documentation
- Security features
- Troubleshooting

#### `QUICKSTART.md`
- Quick start for Docker
- Manual setup for Windows/Linux/macOS
- Common issues and solutions
- Testing procedures
- Performance tuning
- Security hardening

## Data Flow

### Registration Flow
```
register.html (Form)
    ↓ jQuery AJAX
js/register.js (Validation)
    ↓ POST request
php/register.php (Process)
    ↓ Prepared Statement
MySQL Database (Store User)
    ↓ JSON Response
register.js (Show message)
    ↓ Redirect
login.html
```

### Login Flow
```
login.html (Form)
    ↓ jQuery AJAX
js/login.js (Validation)
    ↓ POST request
php/login.php (Authenticate)
    ↓ Prepared Statement + Password Verify
MySQL Database (Fetch User)
    ↓ Generate Token
Redis (Store Session)
    ↓ Return Token
login.js (Save to localStorage)
    ↓ Redirect
profile.html
```

### Profile Flow
```
profile.html (Loaded)
    ↓ jQuery AJAX
js/profile.js (Check Login)
    ↓ POST request
php/profile.php (Get Data)
    ↓ Redis Session Validation
Redis (Get Session)
    ↓ Prepared Statement
MySQL Database (Fetch Profile)
    ↓ Return Data
profile.js (Display Form)
    ↓ User Updates
    ↓ POST request
php/update-profile.php (Update)
    ↓ Prepared Statement
MySQL Database (Save Changes)
    ↓ Response
profile.js (Show Success)
```

## Key Technologies Used

| Component | Technology | Details |
|-----------|-----------|---------|
| Frontend | HTML5 | Semantic markup |
| | CSS3 | Custom + Bootstrap 5 |
| | JavaScript | ES6+ |
| | jQuery | AJAX requests |
| Backend | PHP 8.0+ | Server-side logic |
| Database | MySQL 8.0 | User data storage |
| Session | Redis 7.0 | Session management |
| Security | bcrypt | Password hashing |
| | Prepared Statements | SQL injection prevention |
| | Random Bytes | Token generation |
| Server | Apache/Nginx | Web server |

## Code Organization Principles

1. **Separation of Concerns**
   - HTML: Structure only
   - CSS: Styling only
   - JS: Frontend logic only
   - PHP: Backend logic only
   - Config: Configuration only

2. **No Mixed Code**
   - No PHP in HTML files
   - No CSS in HTML files
   - No JavaScript in HTML files
   - No database queries in frontend

3. **Security First**
   - Prepared statements for all SQL
   - Password hashing for storage
   - Session validation on requests
   - CORS headers configured
   - Input validation

4. **Responsive Design**
   - Mobile-first approach
   - Bootstrap grid system
   - Flexible layouts
   - Touch-friendly buttons

5. **User Experience**
   - Loading spinners
   - Error messages
   - Success notifications
   - Form validation
   - Intuitive navigation

## Standards & Best Practices

✅ **HTML Standards**
- Semantic HTML5 elements
- Proper form structure
- Accessibility attributes

✅ **CSS Standards**
- BEM naming convention
- Mobile-first responsive design
- Bootstrap integration
- Smooth transitions

✅ **JavaScript Standards**
- ES6+ syntax
- Error handling
- Async operations
- Event delegation

✅ **PHP Standards**
- Prepared statements
- Input sanitization
- Proper error handling
- JSON responses
- Comment documentation

✅ **Database Standards**
- Normalized schema
- Proper indexing
- Foreign key constraints
- Transaction support

✅ **Security Standards**
- Password hashing (bcrypt)
- SQL injection prevention
- Session validation
- CORS configuration
- Input validation
