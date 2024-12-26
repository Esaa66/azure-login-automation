# Azure Login Automation

This project automates the login process to an Azure account using Selenium. It supports both password-based login and multi-factor authentication (MFA).

## Project Structure

```
azure-login-automation
├── src
│   ├── login.py        # Automates login using a password
│   ├── mfa.py          # Handles multi-factor authentication
│   └── utils
│       └── helpers.py  # Utility functions for the project
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd azure-login-automation
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure WebDriver:**
   Ensure you have the appropriate WebDriver for your browser installed and available in your system's PATH.

## Usage

1. **Login with Password:**
   Run the `login.py` script to perform a login using just a password.
   ```
   python src/login.py
   ```

2. **Login with MFA:**
   After logging in with a password, the `mfa.py` script can be used to handle the MFA process.
   ```
   python src/mfa.py
   ```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.