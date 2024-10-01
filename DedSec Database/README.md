## What is DedSec Database

DedSec Database is a Flask-based web application designed to manage files through a browser interface. It provides functionality to upload, list, download, and delete files in a simple yet effective manner. The application uses Serveo for tunneling, allowing access to the web interface via a publicly accessible URL.

## Features

- **File Upload**: Upload files to the server.
- **File Listing**: View uploaded files with options to download or delete.
- **File Search**: Search for files by name.
- **Serveo Tunnel**: Exposes the application over the web using Serveo.
- **Responsive Design**: Adapts to various screen sizes with vertical scrolling enabled.

## Requirements

- Python 3.x
- Flask
- Serveo (for tunneling)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/dedsec-database.git
    cd dedsec-database
    ```

2. **Install dependencies:**

    Ensure you have Flask installed. You can install it using pip:

    ```sh
    pip install Flask
    ```

3. **Prepare Serveo:**

    Ensure that you have SSH access and can use Serveo. No special installation is required as Serveo is accessed via SSH.

## Usage

1. **Start the Application:**

    Run the `app.py` script:

    ```sh
    python app.py
    ```

    This will start the Flask server on port 5002 and initiate a Serveo tunnel to provide a public URL for accessing the application.

2. **Access the Application:**

    After starting the application, you will see a Serveo URL in the console output. Use this URL to access the DedSec Database interface.

## File Operations

- **Upload Files**: Use the upload form to select and upload files.
- **Search Files**: Enter a search query in the search box to filter the list of files.
- **Download Files**: Click the "Download" button next to a file to download it.
- **Delete Files**: Click the "Delete" button next to a file to remove it from the server. A confirmation prompt will appear before deletion.

## Code Structure

- `app.py`: Main script to run the Flask application and handle file operations.
- `Database/`: Directory where uploaded files are stored.
- **Functions:**
  - `kill_port(port)`: Terminates processes using the specified port.
  - `start_serveo_tunnel(port)`: Initiates a Serveo tunnel to expose the application.
  - `start_flask_app(port)`: Starts the Flask application server.

## Error Handling

- **File Upload Errors**: Handles cases where no file is selected or an error occurs while saving the file.
- **File Download Errors**: Manages issues related to file access during download.
- **File Deletion Errors**: Deals with errors encountered during file deletion.

## Troubleshooting

- **Port Conflicts**: If the application fails to start, ensure that no other process is using port 5002. The script will attempt to kill processes on this port automatically.
- **Serveo Tunnel Issues**: Check your SSH connection and Serveo setup if the public URL is not generated.