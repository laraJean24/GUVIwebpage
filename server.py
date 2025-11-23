#!/usr/bin/env python3
"""
Simple HTTP Server for User Management System
This serves HTML/CSS/JS files and simulates PHP endpoints with mock data
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import os
import sys
from pathlib import Path

# Mock user database (in-memory)
USERS_DB = {}
SESSIONS = {}

class UserManagementHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        
        # Serve HTML, CSS, JS files normally
        if parsed_path.path.endswith(('.html', '.css', '.js', '.json')):
            return super().do_GET()
        
        return super().do_GET()
    
    def do_POST(self):
        """Handle POST requests for API endpoints"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Read request body
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length).decode('utf-8')
        
        try:
            data = json.loads(body) if body else {}
        except:
            data = {}
        
        # Route to appropriate handler
        if path == '/php/register.php':
            self.handle_register(data)
        elif path == '/php/login.php':
            self.handle_login(data)
        elif path == '/php/profile.php':
            self.handle_profile(data)
        elif path == '/php/update-profile.php':
            self.handle_update_profile(data)
        elif path == '/php/logout.php':
            self.handle_logout(data)
        elif path == '/php/check-email.php':
            self.handle_check_email(data)
        else:
            self.send_error(404, "Endpoint not found")
    
    def handle_register(self, data):
        """Handle user registration"""
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()
        firstName = data.get('firstName', '').strip()
        lastName = data.get('lastName', '').strip()
        
        # Validation
        if not all([email, password, firstName, lastName]):
            return self.send_json({'success': False, 'message': 'All fields required'}, 400)
        
        if len(password) < 6:
            return self.send_json({'success': False, 'message': 'Password must be at least 6 characters'}, 400)
        
        if email in USERS_DB:
            return self.send_json({'success': False, 'message': 'Email already registered'}, 400)
        
        # Store user with actual password (for demo purposes)
        USERS_DB[email] = {
            'firstName': firstName,
            'lastName': lastName,
            'email': email,
            'password': password,  # Store actual password for demo
            'age': None,
            'dob': None,
            'contact': None,
            'address': None,
            'city': None,
            'state': None,
            'zipcode': None,
            'createdAt': str(Path.cwd())
        }
        
        # Auto-login: Generate session token immediately after registration
        import secrets
        token = secrets.token_hex(32)
        SESSIONS[token] = {
            'email': email,
            'userId': email,
            'loginTime': str(Path.cwd())
        }
        
        return self.send_json({
            'success': True,
            'message': '✅ Registration successful! Redirecting to profile...',
            'token': token,
            'autoLogin': True
        })
    
    def handle_login(self, data):
        """Handle user login"""
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()
        
        if not email or not password:
            return self.send_json({'success': False, 'message': 'Email and password required'}, 400)
        
        if email not in USERS_DB:
            return self.send_json({'success': False, 'message': 'Invalid email or password'}, 401)
        
        user = USERS_DB[email]
        
        # Verify password (for demo, direct comparison)
        if password != user['password']:
            return self.send_json({'success': False, 'message': 'Invalid email or password'}, 401)
        
        # Generate session token
        import secrets
        token = secrets.token_hex(32)
        SESSIONS[token] = {
            'email': email,
            'userId': email,  # Using email as ID for demo
            'loginTime': str(Path.cwd())
        }
        
        return self.send_json({
            'success': True,
            'message': '🎉 Login successful! Redirecting to profile...',
            'token': token,
            'user': {
                'firstName': user['firstName'],
                'lastName': user['lastName'],
                'email': user['email']
            }
        })
    
    def handle_profile(self, data):
        """Handle profile fetch"""
        token = data.get('sessionToken', '').strip()
        
        if not token or token not in SESSIONS:
            return self.send_json({'success': False, 'error': 'invalid_session'}, 401)
        
        session = SESSIONS[token]
        email = session['email']
        user = USERS_DB[email]
        
        return self.send_json({
            'success': True,
            'user': {
                'firstName': user['firstName'],
                'lastName': user['lastName'],
                'email': user['email'],
                'age': user['age'],
                'dob': user['dob'],
                'contact': user['contact'],
                'address': user['address'],
                'city': user['city'],
                'state': user['state'],
                'zipcode': user['zipcode']
            }
        })
    
    def handle_update_profile(self, data):
        """Handle profile update"""
        token = data.get('sessionToken', '').strip()
        
        if not token or token not in SESSIONS:
            return self.send_json({'success': False, 'error': 'invalid_session'}, 401)
        
        session = SESSIONS[token]
        email = session['email']
        user = USERS_DB[email]
        
        # Update fields
        if 'age' in data:
            user['age'] = data['age']
        if 'dob' in data:
            user['dob'] = data['dob']
        if 'contact' in data:
            user['contact'] = data['contact']
        if 'address' in data:
            user['address'] = data['address']
        if 'city' in data:
            user['city'] = data['city']
        if 'state' in data:
            user['state'] = data['state']
        if 'zipcode' in data:
            user['zipcode'] = data['zipcode']
        
        return self.send_json({
            'success': True,
            'message': '✅ Profile updated successfully!'
        })
    
    def handle_logout(self, data):
        """Handle logout"""
        token = data.get('sessionToken', '').strip()
        
        if token in SESSIONS:
            del SESSIONS[token]
        
        return self.send_json({
            'success': True,
            'message': 'Logged out successfully'
        })
    
    def handle_check_email(self, data):
        """Check if email exists"""
        email = data.get('email', '').strip()
        
        if not email:
            return self.send_json({'success': False, 'message': 'Email required'}, 400)
        
        exists = email in USERS_DB
        
        return self.send_json({
            'success': True,
            'exists': exists
        })
    
    def send_json(self, data, status=200):
        """Send JSON response"""
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
    
    def do_OPTIONS(self):
        """Handle CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def log_message(self, format, *args):
        """Custom logging"""
        print(f'[{self.log_date_time_string()}] {format % args}')

def run_server(port=8000):
    """Start the server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, UserManagementHandler)
    
    # Test user for demo
    USERS_DB['test@example.com'] = {
        'firstName': 'Test',
        'lastName': 'User',
        'email': 'test@example.com',
        'password': 'password123',  # Demo password
        'age': None,
        'dob': None,
        'contact': None,
        'address': None,
        'city': None,
        'state': None,
        'zipcode': None,
        'createdAt': 'Demo Account'
    }
    
    print(f"""
╔════════════════════════════════════════════════════════════╗
║   User Management System - Development Server              ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  🚀 Server running at: http://localhost:{port}           
║                                                            ║
║  📝 Test Account:                                          ║
║     Email: test@example.com                               ║
║     Password: password123                                  ║
║                                                            ║
║  📖 Documentation: See QUICKSTART.md                       ║
║                                                            ║
║  Press Ctrl+C to stop the server                          ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n\n✋ Server stopped.')
        sys.exit(0)

if __name__ == '__main__':
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f'Invalid port: {sys.argv[1]}. Using default port {port}')
    
    run_server(port)
