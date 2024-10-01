## What is T-Login

T-Login is a Python script designed for secure login management in Termux. It simplifies the setup of username and password credentials, providing a streamlined approach to user authentication. Ideal for users seeking enhanced security for their terminal sessions, T-Login ensures that sensitive information is stored securely through hashing.

##Features

- **Credential Setup**: Easily set up new username and password credentials with simple prompts.
- **Secure Hashing**: Utilizes SHA-256 to hash and store credentials, enhancing security against unauthorized access.
- **Login Validation**: Validates user credentials against stored hashes, ensuring only authorized users can access the terminal.
- **Automated Script Creation**: Automatically creates a login script to manage session authentication seamlessly.
- **Configuration Management**: Modifies the `.bash_profile` to execute the login script on startup.
- **Credential Deletion**: Provides an option to remove credentials and login setups when no longer needed.

## Installation

1. **Prerequisites**:
   - Python 3.x

2. **Clone or Download**:
   - Clone the repository or download the `t-login.py` script to your local machine.

3. **Run the Application**:
   - Navigate to the directory containing `t-login.py`.
   - Make the script executable:
     ```bash
     chmod +x t-login.py
     ```
   - Execute the script with:
     ```bash
     python t-login.py
     ```

## Usage

1. **Set Up Credentials**:
   - Choose the option to set up a new username and password when prompted.

2. **Login Process**:
   - Upon starting your terminal, enter your username and password to authenticate.
   - If the credentials are incorrect, an error message will be displayed, and the terminal will exit, preventing unauthorized access.

3. **Manage Credentials**:
   - Use the provided options to delete or update your credentials as needed.

4. **Exiting**:
   - Exit the application at any time by choosing the exit option from the main menu. 