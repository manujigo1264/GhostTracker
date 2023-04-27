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
    stderr.writelines(f"""{Gr}
       ________               __      ______                __  
      / ____/ /_  ____  _____/ /_    /_  __/________ ______/ /__
     / / __/ __ \/ __ \/ ___/ __/_____/ / / ___/ __ `/ ___/ //_/
    / /_/ / / / / /_/ (__  ) /_/_____/ / / /  / /_/ / /__/ ,<   
    \____/_/ /_/\____/____/\__/     /_/ /_/   \__,_/\___/_/|_|  

              {Wh}[ + ]  Refactored by 0xtron  [ + ]  

        {Wh}[ 1 ] {Gr}IP Tracker

        {Wh}[ 2 ] {Gr}Phone Tracker

        {Wh}[ 0 ] {Gr}Exit
    """)

def track_ip(ip):
    # Retrieve and process IP information
    try:
        req_api = requests.get(f"http://ipwho.is/{ip}")
        ip_data = json.loads(req_api.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    print(f'{Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
    # Print the results
    print(f"{Wh}\n IP target       :{Gr}", ip)
    # ... Additional lines for printing IP information ...
    
def track_phone(phone_number):
    default_region = "ID"

    try:
        parsed_number = phonenumbers.parse(phone_number, default_region)
    except phonenumbers.NumberParseException as e:
        print(f"Error: {e}")
        return

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
    # Print the results
    # ... Additional lines for printing phone number information ...

def main():
    while True:
        os.system('clear')
        print_banner()
        input_user = input(f'\n   {Wh}@Ghost~# {Gr}')

        if input_user == '1':
            os.system('clear')
            ip = input(f"{Wh}\n Enter IP target : {Gr}")
            track_ip(ip)

        elif input_user == '2':
            os.system('clear')
            phone_number = input(f"\n {Wh}Enter phone number target {Gr}Ex [+6281xxxxxxxxx] {Wh}: {Gr}")
            track_phone(phone_number)

        elif input_user == '0':
            print(f"\n  {Wh}[{Ye}!{Wh}] {Ye}THANK'S FOR USING TOOL {Ye}GHOST-TRACK !")
            break

        else:
            print(f" {Ye}Opss no option !")
            time.sleep(2)

if __name__ == '__main__':
    main()
