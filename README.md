# Two-Factor Authentication System

A secure two-factor authentication (2FA) web application built with Flask that implements Time-based One-Time Password (TOTP) authentication using authenticator apps like Google Authenticator or Authy.

## Features

- **User Login** with strong password validation
- **TOTP-Based 2FA** using industry-standard algorithms
- **QR Code Generation** for easy authenticator app setup
- **Session Management** with secure session handling
- **Responsive UI** with a clean, user-friendly interface
- **Dashboard** accessible only after successful 2FA verification

## Password Requirements

Passwords must meet the following criteria:
- Minimum 8 characters long
- At least one uppercase letter
- At least one lowercase letter
- At least one digit (0-9)
- At least one special character (!@#$%^&*()-_+=<>?/{}[]|)

## Tech Stack

- **Backend**: Python 3, Flask
- **Authentication**: PyOTP (TOTP implementation)
- **QR Code Generation**: qrcode library
- **Frontend**: HTML, CSS, JavaScript
- **Session Management**: Flask Sessions

## Project Structure

```
two-factor-auth-system/
├── app.py                 # Main Flask application
├── README.md              # Project documentation
├── static/
│   └── style.css          # Stylesheet
└── templates/
    ├── login.html         # Login page
    ├── otp.html           # OTP verification page
    └── dashboard.html     # User dashboard (post-2FA)
```

## Installation

1. **Clone or download the project**
   ```bash
   cd two-factor-auth-system
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install Flask pyotp qrcode[pil]
   ```

## Running the Application

Start the Flask development server:

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

1. **Login Page** (`/`)
   - Enter your email and a strong password
   - Click "Login"

2. **OTP Setup** (`/otp`)
   - Scan the QR code with an authenticator app (Google Authenticator, Authy, Microsoft Authenticator, etc.)
   - Or manually enter the secret key into your authenticator app
   - Enter the 6-digit OTP code from your authenticator

3. **Verification** (`/verify-otp`)
   - If OTP is correct, you'll be redirected to the dashboard
   - If incorrect, an error message will be displayed

4. **Dashboard** (`/dashboard`)
   - Accessible only after successful 2FA verification
   - Shows user is logged in with 2FA enabled

5. **Logout** (`/logout`)
   - Clears the session and returns to login page

## How 2FA Works

1. **User Login**: User enters email and password
2. **Secret Generation**: A random TOTP secret is generated and stored in the session
3. **QR Code**: The secret is encoded as a provisioning URI and converted to a QR code
4. **Scanner Setup**: User scans the QR code with an authenticator app
5. **OTP Verification**: User enters the 6-digit code from their authenticator
6. **Session Verification**: The code is validated using PyOTP's TOTP algorithm
7. **Access Granted**: Upon successful verification, the user gains access to the dashboard

## Security Notes

⚠️ **Important**: This is a demonstration project. For production use:

- Change the `secret_key` to a secure, random value
- Use environment variables for sensitive configuration
- Implement proper database for user storage
- Add HTTPS/SSL encryption
- Use secure session cookies with proper flags
- Implement rate limiting for login/OTP attempts
- Add CSRF protection
- Implement proper logging and monitoring
- Store user credentials securely (hashed passwords)
- Use a proper secrets management solution

## Dependencies

- **Flask** - Web framework
- **PyOTP** - TOTP/HOTP implementation
- **qrcode** - QR code generation

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## Troubleshooting

**QR Code Not Displaying**
- Ensure `qrcode[pil]` is installed: `pip install qrcode[pil]`

**OTP Verification Fails**
- Check that the authenticator app time is synced
- Ensure you're using the latest OTP code (they expire every 30 seconds)
- Clear browser cookies and try again

**Session Errors**
- Clear browser cookies
- Restart the Flask application

## Future Enhancements

- [ ] Database integration for persistent user storage
- [ ] Backup codes for account recovery
- [ ] Multiple 2FA methods (SMS, Email)
- [ ] Admin panel for user management
- [ ] Audit logging
- [ ] User profile management
- [ ] Password reset functionality

## License

This project is provided as-is for educational and demonstration purposes.

## Author

Created as a demonstration of two-factor authentication implementation.

---

**Last Updated**: February 2026
