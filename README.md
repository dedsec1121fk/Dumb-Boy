## Dumb Boy Features

### Camera Phish
**Camera Phish** is a web application that allows users to capture images using their device's front or back camera. Built with Flask, this tool creates a seamless interface for users to remotely access their camera feed and save captured images directly to their device. 

- **Key Features**:
  - **Camera Access**: Utilizes both front and back cameras to take snapshots, offering versatility for various use cases.
  - **Image Storage**: Captured images are stored in a dedicated directory (`Downloads/Camera-Phish`), making retrieval straightforward.
  - **IP Logging**: Logs the IP address and user agent of each user, providing valuable data for analysis and tracking.
  - **Serveo Integration**: Establishes a secure tunnel for remote access using Serveo, making it easy to share camera access over the internet.
  - **Responsive UI**: Features a user-friendly interface for monitoring the camera feed and capturing images in real time.

### DedSec Database
The **DedSec Database** is a Flask-based web application designed for efficient file management through a browser interface. Users can upload, list, download, and delete files with ease, all facilitated by a simple and effective design.

- **Key Features**:
  - **File Uploading**: Easily upload files to the server, making it a robust tool for document management.
  - **File Listing and Management**: View uploaded files with intuitive options to download or delete, streamlining file operations.
  - **File Search Functionality**: Search for files by name to quickly find what you need without sifting through long lists.
  - **Serveo Tunnel**: Utilizes Serveo to expose the application over the web, allowing remote access via a publicly accessible URL.
  - **Responsive Design**: Adapts to various screen sizes, ensuring a consistent experience across devices.

### Donation Phishing
**Donation Phishing** is an educational tool that demonstrates the collection of personal information through a secure web form. It utilizes Flask to handle form submissions, saving the submitted data in text files while ensuring accessibility via a public URL provided by Serveo.

- **Key Features**:
  - **Form Submission**: Users can submit their personal information, providing a practical example of data collection methods.
  - **Data Storage**: Information is saved in text files within a dedicated `People` directory, organized for easy access.
  - **Serveo Tunneling**: Makes the application accessible from anywhere via a Serveo tunnel, demonstrating remote data collection.
  - **Port Conflict Handling**: Automatically resolves any port conflicts, ensuring smooth operation of the application.

### Customization
This tool is designed to enhance the terminal experience in Termux by updating the `.bashrc` configuration and setting a customized Message of the Day (MOTD). It provides an easy way to personalize your terminal environment.

- **Key Features**:
  - **Custom PS1 Prompt**: Updates the command prompt to display the date, time, username, and current directory, adding a visual flair to the terminal.
  - **ASCII Art MOTD**: Introduces engaging ASCII art to the terminal’s MOTD, making each session more enjoyable and visually appealing.
  - **Error Logging**: Captures any errors encountered during execution, making troubleshooting straightforward.
  - **Termux Compatibility**: Tailored for use in Termux, accommodating its unique file structure and permissions.

### NAIOVUM
**NAIOVUM** simplifies the setup and configuration of Neovim within Termux. It automates the installation of essential packages, plugins, and customized settings, enhancing the coding environment for developers and power users.

- **Key Features**:
  - **Package Installation**: Automatically installs necessary packages like Neovim, Python, and Git, streamlining the initial setup process.
  - **Plugin Management**: Installs popular plugin managers such as Vim-Plug and Packer for hassle-free plugin management.
  - **Custom Configuration**: Sets up a personalized `init.vim` with theme options (like Gruvbox and OneDark) and a selection of useful plugins.
  - **Python Support**: Installs Python support for Neovim, enabling users to leverage Python for scripting and extensions.
  - **Backup and Restore**: Offers functionality to back up and restore Neovim configurations, ensuring users can maintain their settings over time.
  - **Auto-Update Feature**: Automatically updates Neovim and its plugins, keeping the environment up to date.

### OSINTDS
**OSINTDS** is a powerful tool for performing OSINT (Open Source Intelligence) tasks. This application automates the gathering of data from public sources such as emails, phone numbers, social media profiles, and web searches.

- **Key Features**:
  - **Email Lookup**: Validates email addresses and checks if they have been compromised using the "Have I Been Pwned" API, enhancing security awareness.
  - **Instagram Lookup**: Retrieves detailed information from public Instagram profiles, including follower count, bio, and verification status.
  - **IP Lookup**: Geolocates IP addresses, providing details like country, city, ISP, and more, aiding in cybersecurity investigations.
  - **Phone Number Lookup**: Validates phone numbers and retrieves associated carrier, region, and timezone information, useful for various verification processes.
  - **Web Search**: Performs general web searches using Google to quickly retrieve relevant results for a given query.
  - **Username Search**: Checks multiple social media platforms to locate public profiles associated with a given username, enhancing social media investigations.

### T-Login
**T-Login** is a script designed for secure login management within Termux. It simplifies the setup of username and password credentials, providing a secure approach to user authentication.

- **Key Features**:
  - **Credential Setup**: Easily set up new username and password credentials, streamlining the authentication process.
  - **Secure Hashing**: Utilizes SHA-256 to hash and store credentials, enhancing security against unauthorized access.
  - **Login Validation**: Validates user credentials against stored hashes, ensuring that only authorized users can access the terminal environment.
  - **Automated Script Creation**: Automatically generates a login script to manage session authentication seamlessly.
  - **Configuration Management**: Modifies the `.bash_profile` to execute the login script upon startup, ensuring secure access every time the terminal is opened.
  - **Credential Deletion**: Provides options to remove credentials and login setups when they are no longer needed.

## Disclaimer
The **Dumb Boy** project is intended for educational and informational purposes only. Users are encouraged to apply ethical considerations and ensure compliance with local laws and regulations while utilizing these tools. The developer is not responsible for any illegal or unethical actions taken by users of this software. Use these tools responsibly and in accordance with applicable laws.
