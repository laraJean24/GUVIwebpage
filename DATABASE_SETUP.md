# Database Setup Instructions

This document provides step-by-step instructions to set up MySQL and connect it to the application.

## Prerequisites

- MySQL Server (5.7+)
- PHPMyAdmin (optional, but helpful)
- Web Browser
- Text Editor

## Windows Setup (XAMPP)

### Step 1: Install XAMPP
1. Download XAMPP from https://www.apachefriends.org/
2. Run the installer
3. Choose installation folder (default: C:\xampp)
4. Select Apache, MySQL, PHP when prompted
5. Complete installation

### Step 2: Start MySQL
1. Open XAMPP Control Panel
2. Click "Start" next to MySQL
3. You should see "MySQL running"

### Step 3: Create Database
**Method 1: Using PHPMyAdmin**
1. Open http://localhost/phpmyadmin in browser
2. Click "Databases" tab
3. Enter database name: `user_management_db`
4. Click "Create"
5. Import `database-schema.sql`:
   - Click on `user_management_db` database
   - Click "Import" tab
   - Browse to `database-schema.sql`
   - Click "Import"

**Method 2: Using MySQL Command Line**
1. Open Command Prompt
2. Navigate to XAMPP folder: `cd C:\xampp\mysql\bin`
3. Connect to MySQL: `mysql -u root -p`
4. Press Enter (no password by default)
5. Paste and execute these commands:
```sql
CREATE DATABASE IF NOT EXISTS user_management_db;
USE user_management_db;
SOURCE C:\path\to\database-schema.sql;
```

### Step 4: Verify Installation
1. Open PHPMyAdmin: http://localhost/phpmyadmin
2. Click on `user_management_db`
3. You should see `users` table with columns:
   - id, firstName, lastName, email, password
   - age, dob, contact, address, city, state, zipcode
   - createdAt, updatedAt

### Step 5: Configure Application
1. Open `config/db-config.php`
2. Update database credentials if needed:
```php
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', '');
define('DB_NAME', 'user_management_db');
```

## Linux Setup

### Step 1: Install MySQL
```bash
sudo apt-get update
sudo apt-get install mysql-server mysql-client
```

### Step 2: Secure MySQL
```bash
sudo mysql_secure_installation
# Follow prompts to set up security
```

### Step 3: Start MySQL
```bash
sudo systemctl start mysql
sudo systemctl enable mysql  # Start on boot
```

### Step 4: Create Database
```bash
mysql -u root -p < database-schema.sql
```

### Step 5: Verify
```bash
mysql -u root -p user_management_db
SHOW TABLES;
```

## macOS Setup

### Step 1: Install MySQL (Using Homebrew)
```bash
brew install mysql
```

### Step 2: Start MySQL
```bash
brew services start mysql
```

### Step 3: Secure MySQL
```bash
mysql_secure_installation
```

### Step 4: Create Database
```bash
mysql -u root -p < database-schema.sql
```

## Docker Setup (Recommended)

### Step 1: Install Docker
- Download from https://www.docker.com/products/docker-desktop

### Step 2: Run Docker Compose
```bash
cd path/to/Guvi_project
docker-compose up -d
```

### Step 3: Verify Database
```bash
docker-compose exec mysql mysql -u root -proot user_management_db -e "SHOW TABLES;"
```

## Database Connection Test

### Test Connection from PHP
1. Create test file: `test-connection.php`
2. Add this code:
```php
<?php
require_once 'config/db-config.php';

if ($conn->connect_error) {
    echo "Connection failed: " . $conn->connect_error;
} else {
    echo "Connected successfully!";
    
    // Test query
    $result = $conn->query("SELECT COUNT(*) as count FROM users");
    $row = $result->fetch_assoc();
    echo "<br>Total users: " . $row['count'];
}
$conn->close();
?>
```
3. Open http://localhost/Guvi_project/test-connection.php

## Troubleshooting

### "Connection refused" Error
**Issue:** MySQL not running
**Solution:**
- Windows: Start MySQL from XAMPP Control Panel
- Linux: `sudo systemctl start mysql`
- macOS: `brew services start mysql`

### "Access denied for user 'root'" Error
**Issue:** Wrong password
**Solution:**
- Check password in `config/db-config.php`
- Default password for XAMPP is empty
- Reset password: `mysql -u root` (no -p)

### "Database doesn't exist" Error
**Issue:** Database not created
**Solution:**
- Import `database-schema.sql`:
  - PHPMyAdmin: Use Import tab
  - Command line: `mysql -u root -p < database-schema.sql`

### "Table 'users' doesn't exist" Error
**Issue:** Schema not imported
**Solution:**
- Re-run `database-schema.sql`
- Check that import completed successfully

### Port 3306 Already in Use
**Issue:** MySQL port already in use
**Solution:**
- Windows: Check Task Manager for other MySQL process
- Linux: `sudo lsof -i :3306`
- Change port in my.ini or my.cnf

## Security Notes

### Change Default Password
```bash
mysql -u root
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
FLUSH PRIVILEGES;
```

### Create Application User
```bash
mysql -u root -p
CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'app_password';
GRANT ALL PRIVILEGES ON user_management_db.* TO 'appuser'@'localhost';
FLUSH PRIVILEGES;
```

Then update `config/db-config.php`:
```php
define('DB_USER', 'appuser');
define('DB_PASSWORD', 'app_password');
```

## Test Data

The `database-schema.sql` includes a test user:
- **Email:** test@example.com
- **Password:** password123

Use these to test login after setup.

## Backup Database

### Using PHPMyAdmin
1. Click on database name
2. Click "Export" tab
3. Click "Go"
4. Save file

### Using Command Line
```bash
mysqldump -u root -p user_management_db > backup.sql
```

## Restore from Backup
```bash
mysql -u root -p user_management_db < backup.sql
```

## Further Help

- MySQL Docs: https://dev.mysql.com/doc/
- PHPMyAdmin: https://www.phpmyadmin.net/
- Check server error logs for detailed error messages

---

**Next Steps:** Once database is set up, follow QUICKSTART.md to start the application.
