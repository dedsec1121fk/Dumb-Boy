## What is NAIOVUM

NAIOVUM is a Python script designed to streamline the setup and configuration of Neovim on Termux. It automates the installation of essential packages, plugins, and customized settings to enhance the Neovim experience. Perfect for developers and power users, NAIOVUM simplifies the process of configuring a robust coding environment.

## NAIOVUM Features

- **Package Installation**: Automatically installs necessary packages such as Neovim, Python, Git, and more.
- **Plugin Management**: Installs popular plugin managers like Vim-Plug and Packer for easy plugin management.
- **Custom Configuration**: Sets up a personalized `init.vim` with theme options (Gruvbox and OneDark) and useful plugins.
- **Python Support**: Installs Python support for Neovim, allowing users to leverage Python for scripting and extensions.
- **Backup and Restore**: Provides functionality to back up and restore Neovim configurations.
- **Auto-Update**: Automatically updates Neovim and its plugins to the latest versions.
- **Exclusive Configurations**: Adds user-friendly settings for better usability, such as mouse support and clipboard integration.

## Installation

1. **Prerequisites**:
   - Python 3.x
   - Required libraries (install via pip):
     ```bash
     pip install pynvim
     ```

2. **Clone or Download**:
   - Clone the repository or download the script to your local machine.

3. **Run the Application**:
   - Navigate to the directory containing `naiovum.py`.
   - Execute the script with:
     ```bash
     python naiovum.py
     ```

## Usage

1. **Start the Setup**:
   - Upon running the script, you will be prompted to choose a theme for your Neovim setup.

2. **Configuration Steps**:
   - The script will guide you through installing necessary packages, configuring Neovim, and setting up plugins.

3. **Backup/Restore Options**:
   - Utilize the backup and restore features to manage your configurations easily.

4. **Completion**:
   - After the setup, you can start using Neovim by typing `nvim` in your terminal.