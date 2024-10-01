import os
import subprocess

def execute_command(command):
    """Executes a shell command."""
    os.system(command)

def main_menu():
    """Displays the main menu and executes the user's choice."""
    while True:
        print("Choose an option:")
        print("1) Camera Phish - Front")
        print("2) Camera Phish - Back")
        print("3) DedSec Database")
        print("4) Donation Phishing")
        print("5) OSINTDS")
        print("6) NAIOVUM")
        print("7) T-Login")
        print("8) Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            execute_command("cd ~/Dumb Boy/Camera Phish && chmod +x front_camera.py && python front_camera.py")
        elif choice == '2':
            execute_command("cd ~/Dumb Boy/Camera Phish && chmod +x back_camera.py && python back_camera.py")
        elif choice == '3':
            execute_command("cd ~/Dumb Boy/DedSec Database && chmod +x dedsec_database.py && python dedsec_database.py")
        elif choice == '4':
            execute_command("cd ~/Dumb Boy/Donation Phishing && chmod +x donation_phising.py && python donation_phising.py")
        elif choice == '5':
            execute_command("cd ~/Dumb Boy/OSINTDS && chmod +x osintds.py && python osintds.py")
        elif choice == '6':
            execute_command("cd ~/Dumb Boy/NAIOVUM && chmod +x naiovum.py && python naiovum.py")
        elif choice == '7':
            execute_command("cd ~/Dumb Boy/T-Login && chmod +x t-login.py && python t-login.py")
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

