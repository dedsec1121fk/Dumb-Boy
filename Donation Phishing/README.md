## What is Donation Phishing

Donation Phishing is a Python application using Flask that allows users to submit personal information through a secure web form. The application saves the submitted data in text files and uses Serveo to make the local server accessible via a public URL. The app also handles port conflicts to ensure smooth operation.

## Features

- **Form Submission**: Users can submit personal information through a web form.
- **Data Storage**: Information is saved as text files in a `People` directory.
- **Serveo Tunneling**: Exposes the Flask application to the internet using Serveo.
- **Port Conflict Handling**: Automatically resolves port conflicts on port 5000.

## Installation

1. **Prerequisites**:
   - Python 3.x
   - Flask library (install via pip):
     ```bash
     pip install Flask
     ```
   - SSH access to Serveo (no account needed, but ensure SSH is available).

2. **Clone or Download**:
   - Clone the repository or download the application script to your local machine.

3. **Run the Application**:
   - Navigate to the directory containing `app.py`.
   - Execute the script with:
     ```bash
     python app.py
     ```

## Usage

1. **Start the Application**:
   - Run the Python script. The application will:
     - Create a `People` directory if it doesn’t exist.
     - Kill any processes using port 5000 to avoid conflicts.
     - Set up a Serveo tunnel to expose the local Flask server.

2. **Access the Web Form**:
   - Once the server is running, access the web form through the public URL provided by Serveo. The URL will be displayed in your terminal after running the script.

3. **Submit Information**:
   - Fill out the form with the required personal information:
     - First Name
     - Last Name
     - Email
     - Phone Number
     - Birthday (format: DD/MM/YYYY)
   - Optional fields include Social Media Accounts, Height, Weight, Eye Color, Hair Color, and Country.
   - Submit the form.

4. **Data Storage**:
   - The submitted data is saved in text files within the `People` directory, named using the format `FirstName_LastName.txt`.

## Security and Privacy

- **Data Protection**: The application saves data in text files securely.
- **Privacy**: Submitted information is used only for processing and stored securely.

--

## Disclaimer

This application is intended for educational and informational purposes only. The developer of this program is not responsible for any illegal or unethical actions taken by users of this software. Use this tool responsibly and in accordance with all applicable laws.