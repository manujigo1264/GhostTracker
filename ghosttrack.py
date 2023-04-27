#!/usr/bin/env python3
# Improved version of the original script

import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr
import sys

# Separate functions for each functionality
def print_banner():
    stderr.writelines("""
       ________               __      ______                __  
      / ____/ /_  ____  _____/ /_    /_  __/________ ______/ /__
     / / __/ __ \/ __ \/ ___/ __/_____/ / / ___/ __ `/ ___/ //_/
    / /_/ / / / / /_/ (__  ) /_/_____/ / / /  / /_/ / /__/ ,<   
    \____/_/ /_/\____/____/\__/     /_/ /_/   \__,_/\___/_/|_|  

              [ + ]  Refactored by 0xtron  [ + ]  

        [ 1 ] IP Tracker

        [ 2 ] Phone Tracker

        [ 0 ] Exit
    """)

def track_ip(ip):
    # Retrieve and process IP information
    try:
        req_api = requests.get(f"http://ipwho.is/{ip}")
        ip_data = json.loads(req_api.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    print(f'============= SHOW INFORMATION IP ADDRESS =============')
    # Print the results
    print(f"\n IP target       :", ip)
    # ... Additional lines for printing IP information ...
    
def track_phone(phone_number):
    default_region = "ID"

    try:
        parsed_number = phonenumbers.parse(phone_number, default_region)
    except phonenumbers.NumberParseException as e:
        print(f"Error: {e}")
        return

    print(f"\n ========== SHOW INFORMATION PHONE NUMBERS ==========")
    # Print the results
    # ... Additional lines for printing phone number information ...

def main():
    while True:
        os.system('clear')
        print_banner()
        input_user = input('\n   @Ghost~# ')

        if input_user == '1':
            os.system('clear')
            ip = input("\n Enter IP target : ")
            track_ip(ip)

        elif input_user == '2':
            os.system('clear')
            phone_number = input("\n Enter phone number target Ex [+6281xxxxxxxxx] : ")
            track_phone(phone_number)

        elif input_user == '0':
            print("\n  [!] THANK'S FOR USING TOOL GHOST-TRACK !")
            break

        else:
            print(" Opss no option !")
            time.sleep(2)

if __name__ == '__main__':
    main()
