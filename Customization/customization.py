import os
import subprocess
import logging

# Initialize Logging
LOG_FILE = os.path.expanduser("~/.repos_management.log")
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s', handlers=[
    logging.FileHandler(LOG_FILE),
    logging.StreamHandler()
])

# Configuration
HOME_DIR = os.path.expanduser("~")
BASHRC_PATH = os.path.join(HOME_DIR, '.bashrc')

# Enhanced PS1 Prompt
ps1_prompt = r"PS1='🌐 \[\e[1;36m\]\d \[\e[0m\]⏰ \[\e[1;32m\]\t \[\e[0m\]💻 \[\e[1;34m\]dedsec1121fk \[\e[0m\]📂 \[\e[1;33m\]\W \[\e[0m\] : '"

# ASCII Art for the MOTD
DEDSEC_ASCII_ART = r"""
  ___         _ ___           _ _ ___ _ 
 |   \ ___ __| / __| ___ __  / / |_  ) |
 | |) / -_) _` \__ \/ -_) _| | | |/ /| |
 |___/\___\__,_|___/\___\__| |_|_/___|_|
"""

def run_command(command, description=""):
    """Run a shell command with logging and error handling."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True)
        return result
    except subprocess.CalledProcessError as e:
        error_message = e.stderr.decode().strip()
        logging.error(f"Error executing {description or command}: {error_message}")
        return None

def update_bashrc():
    """Update the .bashrc file to set the custom PS1 prompt and MOTD display check."""
    motd_check = """if [ -z "$MOTD_DISPLAYED" ]; then
    cat /data/data/com.termux/files/usr/etc/motd
    export MOTD_DISPLAYED=1
fi
"""
    try:
        with open(BASHRC_PATH, "a") as bashrc:
            # Check if the MOTD check already exists
            with open(BASHRC_PATH, "r") as read_bashrc:
                content = read_bashrc.read()
                if motd_check.strip() not in content:
                    bashrc.write(f"\n# Custom PS1 Prompt\n{ps1_prompt}\n\n{motd_check}\n")
                else:
                    logging.info("MOTD check already exists in .bashrc.")
    except PermissionError:
        logging.error("Permission denied: Unable to update the .bashrc file.")
    except FileNotFoundError:
        logging.error("~/.bashrc file not found.")

def update_motd():
    """Update the MOTD with ASCII art."""
    motd_path = "/data/data/com.termux/files/usr/etc/motd"  # Adjust for Termux-specific path
    try:
        with open(motd_path, "w") as motd_file:
            motd_file.write(DEDSEC_ASCII_ART)
    except PermissionError:
        logging.error("Permission denied: Run the script with Termux permissions to update the MOTD file.")

def main():
    """Main function to execute the script tasks."""
    update_bashrc()
    update_motd()

if __name__ == "__main__":
    main()

