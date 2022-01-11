"""
Wireless Network Scanner for Windows
"""

import subprocess
import os
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

"""
Blank input so user can return to menu by hitting "enter" when they are ready
Clear Screen in each function to keep UI looking clean
Accept bad input without throwing error, pass exceptions to try again



We're using the subprocess module to do the same thing we can do in windows command prompt.

https://www.webservertalk.com/netsh-wlan-commands
https://www.techgeekbuzz.com/how-to-build-a-wifi-scanner-in-python/
https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands
https://docs.python.org/3/library/subprocess.html

"""

def call_menu():
    no_inp = input("Press enter to continue.") # Just a blank input that does nothing but wait until user presses enter key before calling next functions.
    clearConsole()
    menu()
    

def show_available_networks():
    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])

    decoded_networks = networks.decode('ascii')

    print(decoded_networks)

    call_menu()

def show_interface_information():
    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces'])

    decoded_networks = networks.decode('ascii')

    print(decoded_networks)
    
    call_menu()
    
def show_network_drivers():
    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'drivers'])

    decoded_networks = networks.decode('ascii')

    print(decoded_networks)

    call_menu()
    
def show_network_capabilitiess():
    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'wirelesscapabilities'])

    decoded_networks = networks.decode('ascii')

    print(decoded_networks)

    call_menu()
    
def show_network_profiles():
    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

    decoded_networks = networks.decode('ascii')

    print(decoded_networks)

    call_menu()
    
def show_network_password():
    while True:
        ssid_input = input("Enter SSID to view password: ")
        try:
            networks = subprocess.check_output(['netsh', 'wlan', 'show', 'profile','name='+ssid_input,'key=clear'])

            decoded_networks = networks.decode('ascii')

            print(decoded_networks)
            break
        except:
            print("Invalid input, please try again.")

    call_menu()
    
def menu():
    # Print menu at top of screen
    # Use number options for selection

    print("PYTHON WINDOWS NETWORK SCANNER by zultone\n\nMenu Options")
    print("1. Show Available Networks, 2. Show Interface Info, 3. Show Network Drivers, \n4. Show Network Capabilities, 5. Show Profiles, 6. Show Network Password")
    print("\n\n\n\n\n\n")
    while True:
        opt_inp = input("Enter number of your selection: ")
        
        if opt_inp == "1":
            clearConsole()
            show_available_networks()
            break
        elif opt_inp == "2":
            clearConsole()
            show_interface_information()
            break
        elif opt_inp == "3":
            clearConsole()
            show_network_drivers()
            break
        elif opt_inp == "4":
            clearConsole()
            show_network_capabilitiess()
            break
        elif opt_inp == "5":
            clearConsole()
            show_network_profiles()
            break
        elif opt_inp == "6":
            clearConsole()
            show_network_password()
            break
        else:
            clearConsole()
            print("Invalid Selection, check your options and try again.\n")
            print("Menu Options")
            print("1. Show Available Networks, 2. Show Interface Info, 3. Show Network Drivers, \n4. Show Network Capabilities, 5. Show Profiles, 6. Show Network Password")
            print("\n\n\n\n\n\n")
            
menu()
