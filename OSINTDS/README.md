## What is OSINTDS

OSINTDS is a Python tool for performing OSINT (Open Source Intelligence) tasks. It automates data gathering from public sources like emails, phone numbers, social media profiles, IP addresses, and web searches. Ideal for cybersecurity pros, investigators, or anyone exploring public data, it simplifies OSINT operations.

#OSINTDS Features

- **Email Lookup**: Validate email addresses and check if they've been compromised using the "Have I Been Pwned" API.
- **Instagram Lookup**: Retrieve detailed information from public Instagram profiles, including follower count, bio, and verification status.
- **IP Lookup**: Geolocate IP addresses and obtain information such as country, city, ISP, and more.
- **Phone Number Lookup**: Validate phone numbers and retrieve associated carrier, region, and timezone information.
- **Web Search**: Perform a general web search using Google to quickly retrieve results for a given query.
- **Username Search**: Check multiple social media platforms to locate public profiles associated with a given username.

## Installation

1. **Prerequisites**:
   - Python 3.x
   - Required libraries (install via pip):
     ```bash
     pip install requests phonenumbers googlesearch-python six
     ```

2. **Clone or Download**:
   - Clone the repository or download the script to your local machine.

3. **Run the Application**:
   - Navigate to the directory containing `OSINTDS.py`.
   - Run the script with:
     ```bash
     python OSINTDS.py
     ```

## Usage

1. **Start the Application**:
   - Upon running the script, you will be presented with a menu to choose the desired OSINT operation.
   
2. **Available Operations**:
   - **Email Lookup**: Input an email address to validate and check if it has been pwned.
   - **Instagram Lookup**: Enter a username to retrieve public data from their Instagram profile.
   - **IP Lookup**: Input an IP address to get geolocation details.
   - **Phone Number Lookup**: Enter a phone number to validate and get carrier, region, and timezone info.
   - **Web Search**: Provide a search query to retrieve top 10 search results from Google.
   - **Username Search**: Input a username and check its presence on popular social media platforms.

3. **Exit**: Choose option `7` to quit the application.

## Security and Privacy

- **Public Data**: The application retrieves publicly available data from the internet and OSINT sources. No private data is accessed or stored.
- **Ethical Use**: Ensure compliance with local laws and regulations while using the application. 

## Disclaimer

This tool is intended for educational purposes only. The developer assumes no responsibility for any unethical or illegal activities conducted with this software. Always use OSINT tools responsibly and within the legal framework of your jurisdiction.