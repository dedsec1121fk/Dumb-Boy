## What is Camera Phish

Camera Phish is a simple web application designed to capture images using a device's front or back camera. The application leverages Flask to provide a seamless interface for image capture and storage, enabling users to remotely access their camera feed and save captured images directly to their device.

## Features

- **Camera Access**: Utilizes the device's front and back cameras to capture images.
- **Image Storage**: Captured images are saved in a dedicated directory (`Downloads/Camera-Phish`).
- **IP Logging**: Logs the IP address and user agent of each user accessing the application.
- **Serveo Integration**: Establishes a secure tunnel for remote access using Serveo.
- **Responsive UI**: Provides a user-friendly interface for viewing the camera feed and capturing images.

## File Descriptions

### `front_camera.py`
This script implements the front camera functionality. Key components include:

- **Flask Application**: Sets up the web server to handle requests and serve the HTML interface.
- **HTML Interface**: Uses JavaScript to access the front camera, display the live video feed, and capture images every 1.5 seconds.
- **Image Processing**: Captured images are processed and saved as PNG files with a timestamp in the `Downloads/Camera-Phish` folder.
- **IP Logging**: Records the IP address and user agent of each visitor to the application.
- **Serveo Tunnel**: Establishes a remote access link to the application via Serveo.

### `back_camera.py`
This script mirrors the functionality of `front_camera.py`, with the primary difference being that it utilizes the device's back camera for image capture. It shares the same structure and logic, ensuring consistency in functionality and user experience.

## Usage

- Open the Serveo link in a web browser.
- Allow camera permissions when prompted.
- The application will automatically start capturing images and saving them in the specified folder.

## Disclaimer

**Camera Phish** is intended for educational purposes only. Please ensure compliance with privacy laws and regulations before using this application. Unauthorized access to a camera without consent is illegal and unethical.