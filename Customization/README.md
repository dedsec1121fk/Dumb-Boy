## What is Customization

Customization is a Python script designed to enhance the terminal experience by updating the `.bashrc` configuration and setting a customized Message of the Day (MOTD) in Termux. It automates the setup of a visually appealing prompt and informative ASCII art, perfect for developers and terminal users seeking a more personalized environment.

##Features

- **Custom PS1 Prompt**: Sets an enhanced prompt that displays the date, time, username, and current directory, adding visual flair to your terminal.
- **ASCII Art MOTD**: Updates the terminal's MOTD with engaging ASCII art, making your terminal sessions more enjoyable.
- **Error Logging**: Logs any errors encountered during script execution to a designated log file, ensuring troubleshooting is straightforward.
- **Compatibility**: Specifically tailored for use in Termux, accommodating its unique file structure and permissions.

## Installation

1. **Prerequisites**:
   - Python 3.x installed on your system.

2. **Clone or Download**:
   - Clone the repository or download the `customization.py` script to your local machine.

3. **Run the Application**:
   - Navigate to the directory containing `customization.py`.
   - Execute the script with:
     ```bash
     python customization.py
     ```

## Usage

1. **Run the Script**:
   - Simply execute the script to automatically update your `.bashrc` and set the MOTD.

2. **Check the Changes**:
   - Open a new terminal session to see the updated prompt and MOTD.

3. **Logging**:
   - Check the log file at `~/.repos_management.log` for any execution errors or messages.

With this script, you can easily personalize your terminal experience and enjoy a more vibrant interface every time you open your shell.