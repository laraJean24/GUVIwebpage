# Quick Start Guide

## Option 1: Using Docker (Recommended)

### Prerequisites
- Docker Desktop installed

### Steps
1. **Navigate to project directory**
   ```bash
   cd path/to/Guvi_project
   ```

2. **Start Docker containers**
   ```bash
   docker-compose up -d
   ```

3. **Wait for services to be ready** (30 seconds)

4. **Access the application**
   ```
   http://localhost/Guvi_project/index.html
   ```

5. **Test credentials**
   - Email: test@example.com
   - Password: password123

6. **Stop containers**
   ```bash
   docker-compose down
   ```

---

## Option 2: Manual Setup

### Prerequisites
- PHP 8.0+ with mysqli and redis extensions
- MySQL 8.0+
- Redis 7.0+
- Apache/Nginx web server

### Windows Setup (XAMPP)

1. **Install XAMPP**
   - Download from https://www.apachefriends.org/
   - Run installer and enable PHP, MySQL, Apache

2. **Install Redis**
   - Download from https://github.com/microsoftarchive/redis/releases
   - Extract to a folder and add to PATH or create batch file to start

3. **Copy project files**
   ```
   C:\xampp\htdocs\Guvi_project\
   ```

4. **Create database**
   - Open phpMyAdmin: http://localhost/phpmyadmin
   - Import `database-schema.sql`

5. **Configure PHP**
   - Ensure `php.ini` has:
     ```
     extension=mysqli
     extension=redis
     ```

6. **Start services**
   - Start XAMPP Control Panel
   - Start Apache and MySQL
   - Start Redis (redis-server.exe)

7. **Access application**
   ```
   http://localhost/Guvi_project/index.html
   ```

### Linux Setup

1. **Install dependencies**
   ```bash
   sudo apt-get update
   sudo apt-get install apache2 mysql-server redis-server php php-mysql php-redis
   ```

2. **Enable Apache modules**
   ```bash
   sudo a2enmod rewrite
   sudo a2enmod headers
   ```

3. **Copy project files**
   ```bash
   sudo cp -r Guvi_project /var/www/html/
   sudo chown -R www-data:www-data /var/www/html/Guvi_project
   ```

4. **Create database**
   ```bash
   mysql -u root -p < database-schema.sql
   ```

5. **Update database credentials** in `config/db-config.php`

6. **Start services**
   ```bash
   sudo systemctl start apache2
   sudo systemctl start mysql
   sudo systemctl start redis-server
   ```

7. **Access application**
   ```
   http://localhost/Guvi_project/index.html
   ```

### macOS Setup

1. **Install dependencies** (using Homebrew)
   ```bash
   brew install apache2 mysql redis php
   ```

2. **Copy project files**
   ```bash
   sudo cp -r Guvi_project /Library/WebServer/Documents/
   ```

3. **Create database**
   ```bash
   mysql -u root < database-schema.sql
   ```

4. **Start services**
   ```bash
   brew services start apache2
   brew services start mysql
   brew services start redis
   ```

5. **Access application**
   ```
   http://localhost/Guvi_project/index.html
   ```

---

## Common Issues & Solutions

### 1. "Database connection failed"
**Solution:**
- Check MySQL is running
- Verify credentials in `config/db-config.php`
- Run: `mysql -u root -p user_management_db < database-schema.sql`

### 2. "Redis connection failed"
**Solution:**
- Check Redis is running: `redis-cli ping`
- Should return "PONG"
- Verify host and port in `config/redis-config.php`

### 3. "PHP mysqli extension not found"
**Solution:**
- Windows (XAMPP): Edit php.ini and uncomment `;extension=mysqli`
- Linux: `sudo apt-get install php-mysql`
- macOS: `brew install php@8.0 php@8.0-mysql`

### 4. "PHP redis extension not found"
**Solution:**
- Windows: Download redis.dll for your PHP version
- Linux: `sudo apt-get install php-redis` or `sudo pecl install redis`
- macOS: `brew install php@8.0 php@8.0-redis`

### 5. AJAX requests showing 404
**Solution:**
- Check php files are in correct folder: `Guvi_project/php/`
- Verify web server is serving the folder correctly
- Check browser console (F12) for exact error

### 6. Session token not working
**Solution:**
- Clear browser localStorage: DevTools → Application → Storage → Clear
- Ensure Redis is running
- Try logging in again

### 7. "Permission Denied" errors
**Solution:**
- Linux/macOS: `sudo chown -R www-data:www-data /path/to/Guvi_project`
- Windows: Run Command Prompt as Administrator

---

## Testing the Application

### Registration Flow
1. Click "Create New Account"
2. Fill form with:
   - First Name: John
   - Last Name: Doe
   - Email: john@example.com
   - Password: test123
   - Confirm: test123
3. Click Register
4. Should see success message and redirect to login

### Login Flow
1. Go to login page
2. Enter: john@example.com / test123
3. Should be redirected to profile page
4. Session token visible in browser DevTools → Application → LocalStorage

### Profile Update
1. From profile page
2. Fill additional fields (age, dob, etc.)
3. Click "Save Changes"
4. Should see success message

### Logout
1. Click "Logout" button
2. Should redirect to login page
3. Session token removed from localStorage

---

## Performance Tuning

### Enable Query Caching (MySQL)
Add to `my.ini` or `my.cnf`:
```ini
[mysqld]
query_cache_type = 1
query_cache_size = 16M
```

### Optimize PHP
Edit `php.ini`:
```ini
memory_limit = 256M
max_execution_time = 30
upload_max_filesize = 20M
opcache.enable = 1
```

### Redis Configuration
Edit `redis.conf`:
```
maxmemory 256mb
maxmemory-policy allkeys-lru
```

---

## Security Hardening

1. **Change Database Password**
   - Update in `config/db-config.php`
   - Set strong password in MySQL

2. **Change Redis Password**
   - Set requirepass in redis.conf
   - Update in `config/redis-config.php`

3. **Enable HTTPS**
   - Get SSL certificate
   - Update .htaccess for HTTP→HTTPS redirect

4. **Set Proper Permissions**
   ```bash
   chmod 750 /path/to/Guvi_project
   chmod 644 /path/to/Guvi_project/*.html
   chmod 644 /path/to/Guvi_project/css/*
   chmod 644 /path/to/Guvi_project/js/*
   chmod 644 /path/to/Guvi_project/php/*
   chmod 600 /path/to/Guvi_project/config/*
   ```

---

## Monitoring & Debugging

### View PHP Error Logs
```bash
# Linux/macOS
tail -f /var/log/apache2/error.log

# Windows (XAMPP)
C:\xampp\apache\logs\error.log
```

### View MySQL Logs
```bash
# Linux
tail -f /var/log/mysql/error.log

# macOS
tail -f /usr/local/var/mysql/error.log
```

### Monitor Redis
```bash
redis-cli MONITOR
```

### Check Database
```bash
mysql -u root -p user_management_db
SELECT * FROM users;
```

---

## Useful Commands

### MySQL
```bash
# Connect
mysql -u root -p

# Select database
USE user_management_db;

# View users
SELECT * FROM users;

# Clear users
DELETE FROM users;

# Reset auto_increment
ALTER TABLE users AUTO_INCREMENT = 1;
```

### Redis
```bash
# Connect
redis-cli

# View all sessions
KEYS session:*

# View specific session
GET session:[token]

# Clear all sessions
FLUSHDB

# Monitor commands
MONITOR
```

---

## Support

If you encounter issues not covered here:
1. Check the detailed README.md
2. Review code comments in PHP files
3. Check browser console (F12) for errors
4. Review server error logs
5. Verify all services are running
