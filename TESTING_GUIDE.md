# 🧪 Complete Testing Guide

## Testing the User Management System

Follow these steps to test the complete flow of the application:

---

## **Phase 1: Registration Test**

### Create a New Account
1. **Go to Registration Page**: http://localhost:8000/register.html
2. **Fill in the form**:
   - First Name: `John`
   - Last Name: `Doe`
   - Email: `john@example.com`
   - Password: `password123`
   - Confirm Password: `password123`

3. **Email Validation**:
   - When you blur from the email field, you should see:
     - ✅ Green checkmark if email is available
     - ❌ Red X if email is already registered

4. **Click "Register Now"** button
   - You should see: "Registering..." with a spinner
   - Success message: "✅ Registration successful! Redirecting to profile..."

5. **Automatic Redirect**:
   - After 1.5 seconds, you should be automatically redirected to your profile page
   - **No login needed!** (Auto-login feature)

---

## **Phase 2: Profile Page Test**

### Profile Page Features

#### 2.1 **Profile Photo Upload**
1. Click the camera icon (📷) on your profile photo
2. Select an image from your computer (JPG, PNG, GIF, WebP)
3. File size must be less than 5MB
4. Photo preview appears immediately
5. Photo is saved to browser storage (persists on reload)

#### 2.2 **Profile Information**
Your profile displays:
- **Profile Photo**: Circular image with upload capability
- **Name**: Auto-populated from registration (read-only)
- **Email**: Auto-populated from registration (read-only)
- **Stats Section**: 
  - 100% Profile (completion indicator)
  - ✅ Verified (account status)
  - 🔒 Secure (security status)

#### 2.3 **Edit Profile Fields**

You can edit these sections:

**📋 Personal Details:**
- Age: Enter your age (1-120)
- Date of Birth: Select a date

**📞 Contact Information:**
- Phone Number: Format like +1 (555) 000-0000

**🏠 Address Information:**
- Street Address: Your residential address
- City: Your city name
- State/Province: State abbreviation (e.g., NY)
- Zip/Postal Code: Postal code

#### 2.4 **Save Changes**
1. Fill in the optional fields
2. Click **"💾 Save Changes"** button
3. Success message appears: "✅ Profile updated successfully!"
4. Message auto-dismisses after 5 seconds

#### 2.5 **Reset Form**
- Click **"🔄 Reset"** button to revert all changes to saved values

---

## **Phase 3: Login Test (For Existing Accounts)**

### Using Existing Account
1. Go to: http://localhost:8000/login.html
2. **Email**: `test@example.com`
3. **Password**: `password123`
4. Click **"Login"** button
5. You should see: "🎉 Login successful! Redirecting to profile..."
6. Redirected to profile page after 1 second

### Using Your Registered Account
1. Go to login page
2. Use your registered email and password
3. Should log in successfully and go to profile

---

## **Phase 4: Logout Test**

1. On profile page, click **"🚪 Logout"** button in navbar
2. Session token is cleared
3. You are redirected to login page
4. Trying to access profile page directly will redirect you to login

---

## **Phase 5: Session Management Test**

### Session Persistence
1. Register and go to profile page
2. Refresh the page (F5 or Ctrl+R)
3. Profile should load without re-login (session persists)

### Session Expiration
1. Manually clear localStorage in browser console:
   ```javascript
   localStorage.removeItem('sessionToken');
   localStorage.removeItem('userEmail');
   ```
2. Refresh profile page
3. You should be redirected to login page

---

## **Test Credentials**

### Pre-loaded Test Account
- **Email**: `test@example.com`
- **Password**: `password123`
- This account is pre-loaded in the system

### Test With Multiple Accounts
Create 2-3 test accounts with different emails to verify:
- Registration for each account works
- Each account has separate profile data
- Profile photo upload works independently per account
- Logout and login with different accounts works

---

## **Expected Behavior Checklist**

### ✅ Registration Flow
- [ ] Form validates all fields are filled
- [ ] Password minimum 6 characters enforced
- [ ] Password confirmation must match
- [ ] Email format validated
- [ ] Email availability checked in real-time (✅/❌ indicator)
- [ ] Cannot register with existing email
- [ ] Success message shows after registration
- [ ] Auto-login occurs (session token generated)
- [ ] Redirects to profile page after 1.5 seconds

### ✅ Profile Page
- [ ] Profile loads immediately after registration
- [ ] User name and email display correctly
- [ ] All editable fields are empty initially (no data)
- [ ] Basic fields (first name, last name, email) are disabled
- [ ] Photo upload works and shows preview
- [ ] Photo persists on page refresh
- [ ] Can edit personal details (age, DOB)
- [ ] Can edit contact information (phone)
- [ ] Can edit address information (street, city, state, zip)
- [ ] Save changes shows success message
- [ ] Reset button reverts to last saved values

### ✅ Login Flow
- [ ] Email and password required
- [ ] Email validation on input
- [ ] Password field hidden (dots/asterisks)
- [ ] Error message for invalid credentials
- [ ] Success message after login
- [ ] Redirects to profile after 1 second
- [ ] Can login with registered email/password

### ✅ Logout Flow
- [ ] Logout button visible in navbar
- [ ] Clicking logout clears session
- [ ] Redirects to login page
- [ ] Cannot access profile without login

### ✅ UI/UX Features
- [ ] Beautiful gradient backgrounds
- [ ] Profile header with gradient
- [ ] Circular profile photo with border
- [ ] Camera icon overlay on photo
- [ ] Responsive design on mobile/tablet/desktop
- [ ] Form labels with emojis for visual hierarchy
- [ ] Color-coded alerts (success = green, error = red)
- [ ] Loading spinner shows while loading profile
- [ ] Smooth transitions and animations
- [ ] Professional card design with shadows

---

## **Testing On Different Browsers**

Test the application on:
- [ ] Chrome/Chromium
- [ ] Firefox
- [ ] Edge
- [ ] Safari (if on Mac)

**Note**: All features should work identically across browsers.

---

## **Mobile/Responsive Testing**

1. Open DevTools (F12)
2. Toggle Device Toolbar (Ctrl+Shift+M)
3. Test on different screen sizes:
   - [ ] Mobile (375px) - iPhone SE
   - [ ] Tablet (768px) - iPad
   - [ ] Desktop (1024px+) - Standard desktop

**Expected**: All forms should stack vertically on mobile, side-by-side on desktop.

---

## **Common Issues & Solutions**

### Issue: Profile page shows "Loading your profile..." indefinitely
**Solution**: 
- Check browser console (F12 → Console) for errors
- Verify sessionToken exists: `localStorage.getItem('sessionToken')`
- Try logging in again

### Issue: Photo upload doesn't work
**Solution**:
- Check file size (must be < 5MB)
- Check file type (JPEG, PNG, GIF, WebP only)
- Check browser console for errors

### Issue: Changes not saving
**Solution**:
- Check alert messages for validation errors
- Verify all required fields are filled
- Try refreshing and saving again

### Issue: Can't register with existing email
**Solution**:
- This is intentional! Each email can only register once
- Try with a different email address

### Issue: Session expires/redirects to login
**Solution**:
- This is normal behavior if sessionToken is cleared
- Register/login again

---

## **Performance Testing**

1. **Page Load Time**:
   - Open DevTools (F12 → Network tab)
   - Refresh page
   - Monitor load time (should be < 1 second)

2. **AJAX Response Time**:
   - Check Network tab
   - Registration POST should respond in < 500ms
   - Profile POST should respond in < 200ms

3. **Image Upload**:
   - Large images should process quickly
   - Preview should appear immediately

---

## **Security Testing**

### ✅ Verify These Security Features
1. **Password Hashing**: Passwords not stored as plain text ✅
2. **Session Tokens**: 64-character hex tokens (unique per login) ✅
3. **Email Validation**: No duplicate account emails allowed ✅
4. **Input Validation**: All inputs validated before processing ✅
5. **XSS Protection**: HTML special characters handled properly ✅
6. **CSRF Protection**: POST endpoints require sessionToken ✅

### Manual Security Test
1. Try to access profile.html directly without login
   - Should redirect to login page
2. Try to modify sessionToken in localStorage
   - Profile should not load or redirect to login
3. Try to bypass password validation
   - System should reject with error

---

## **Final Verification**

Before submitting the project:
- [ ] All 3 pages (register, login, profile) load without errors
- [ ] Complete registration flow works (register → profile)
- [ ] Complete login flow works (login → profile)
- [ ] Profile photo upload works
- [ ] Profile updates save correctly
- [ ] Logout works and clears session
- [ ] Responsive design works on all screen sizes
- [ ] No console errors in browser (F12)
- [ ] All UI elements are properly styled
- [ ] Gradients and colors display correctly
- [ ] All buttons and links work
- [ ] Form validation works as expected

---

## **Test Data**

### Create Multiple Test Accounts
Use these test emails to create multiple accounts:

```
1. john@example.com / password123
2. jane@example.com / securePass456
3. test.user@example.com / TestPass789
4. demo@example.com / DemoPass000
```

---

## **Getting Support**

If something doesn't work:
1. Check browser console (F12 → Console tab) for error messages
2. Check terminal where server is running for any errors
3. Verify server is still running (http://localhost:8000 should load)
4. Try clearing browser cache (Ctrl+Shift+Delete)
5. Try in a fresh browser window/incognito mode

---

## **Success Criteria**

✅ **All of the following must be true**:
1. Registration works → Auto-login → Profile page loads
2. Profile page displays user information correctly
3. Profile photo upload and display works
4. Profile updates save successfully
5. Login with existing credentials works
6. Logout clears session and redirects
7. UI is professional and responsive
8. No console errors
9. All validations work as expected
10. Session management works correctly

**Once all criteria are met, the project is ready for submission!** 🎉

