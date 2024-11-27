import subprocess
import sys
import time
import os
import requests
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor

# Initialize colorama
init(autoreset=True)

# Function to clear the screen
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/MacOS
        os.system('clear')

# Function to show logo
def show_logo():
    logo = '''
███████╗██╗   ██╗██████╗ ██████╗ ██╗ ██████╗  ██████╗ ███████╗██████╗
██╔════╝██║   ██║██╔══██╗██╔══██╗██║██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
███████╗██║   ██║██████╔╝██║  ██║██║██║  ███╗██║  ███╗█████╗  ██████╔╝
╚════██║██║   ██║██╔══██╗██║  ██║██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
███████║╚██████╔╝██████╔╝██████╔╝██║╚██████╔╝╚██████╔╝███████╗██║  ██║
╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
           \033[32mpазработано @ARTIST для INFLUXION"\033[0m
    '''
    print(Fore.RED + logo)  # Use RED for the logo color

# Function to simulate rotating circle animation
def rotating_circle():
    circle = ['◯', '◔', '◑', '◕']
    for _ in range(10):
        for i in range(len(circle)):
            sys.stdout.write(f'\r{Fore.GREEN}Enumerating subdomains... {circle[i]}')
            sys.stdout.flush()
            time.sleep(0.5)

# Function to get subdomains using Sublist3r
def get_subdomains(domain):
    try:
        # Run Sublist3r tool to get subdomains
        result = subprocess.run(
            ['sublist3r', '-d', domain, '-t', '10', '-o', 'subdomains.txt'],  # '-t' sets the threads for faster results
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            print(Fore.RED + "Error running Sublist3r: " + result.stderr)
            return []

        # Read the subdomains from the output file
        with open('subdomains.txt', 'r') as file:
            subdomains = [line.strip() for line in file.readlines()]

        return subdomains

    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        return []

# Function to check if a subdomain is live
def check_subdomain(subdomain):
    url = f"http://{subdomain}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(Fore.GREEN + f"Live Subdomain: {subdomain}")  # Print live subdomain immediately
            return subdomain
    except requests.RequestException:
        pass
    return None

# Function to filter out invalid or unrelated subdomains
def filter_subdomains(subdomains, domain):
    # Filter out subdomains that do not belong to the given domain (e.g., google.com subdomains)
    return [sub for sub in subdomains if sub.endswith(domain)]

# Function to show live subdomains
def show_live_subdomains(subdomains, domain):
    live_subdomains = []
    if subdomains:
        # Use ThreadPoolExecutor to check subdomains concurrently
        with ThreadPoolExecutor(max_workers=10) as executor:
            live_subdomains = list(executor.map(check_subdomain, subdomains))

        # Filter out None values (subdomains that are not live)
        live_subdomains = [sub for sub in live_subdomains if sub]

    if not live_subdomains:
        print(Fore.RED + "No live subdomains found.")
    return live_subdomains

# Function to get user input for domain
def get_domain():
    domain = input(Fore.YELLOW + "\nEnter the domain (e.g., example.com): ").strip()
    if not domain:
        print(Fore.RED + "Domain cannot be empty!")
        return None
    return domain

# Function to ask the user if they want to exit or go back to the main menu
def ask_to_exit_or_menu():
    choice = input(Fore.YELLOW + "\nWould you like to (E)xit or (M)ain Menu? ").strip().lower()
    if choice == 'e':
        print(Fore.GREEN + "Exiting... Goodbye!")
        sys.exit(0)  # Exit the program
    elif choice == 'm':
        return True
    else:
        print(Fore.RED + "Invalid choice. Please enter 'E' to exit or 'M' for the main menu.")
        return False

# Main function
def main():
    clear_screen()  # Clear screen at the start
    show_logo()  # Show logo
    time.sleep(2)  # Wait for 2 seconds to show the logo

    while True:  # Keep asking for domain and checking until user exits or goes to main menu
        domain = get_domain()  # Get domain from the user
        if not domain:
            return  # Exit if no domain is entered

        # Start the rotating circle animation while we get subdomains
        rotating_circle()  # Show rotating circle for animation

        # Get subdomains using Sublist3r
        subdomains = get_subdomains(domain)

        if subdomains:
            # Filter out unrelated subdomains (e.g., subdomains of google.com if entered example.com)
            subdomains = filter_subdomains(subdomains, domain)

            # Show live subdomains as they are found
            show_live_subdomains(subdomains, domain)

            # Ask if the user wants to exit or go back to the main menu
            if not ask_to_exit_or_menu():
                continue  # If user chooses to go back to menu, continue the loop
        else:
            print(Fore.RED + "No subdomains found.")

if __name__ == "__main__":
    main()
