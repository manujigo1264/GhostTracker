import json
import os
import requests
import sys
import time
import phonenumbers
from phonenumbers import carrier, geocoder, timezone, number_type

def print_banner():
    sys.stderr.write("""
    ***********************************************
    *          IP and Phone Number Tracker        *
    *               @WRITTEN BY 0XTRON            *
    ***********************************************
    """)

def track_ip(ip):
    try:
        req_api = requests.get(f"http://ip-api.com/json/{ip}")
        ip_data = json.loads(req_api.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    if ip_data['status'] == 'fail':
        print("Error: IP not found")
        return

    print(f'\n============= DETAILED INFORMATION IP ADDRESS =============')
    for key, value in ip_data.items():
        print(f" {key.capitalize(): <16}: {value}")

def track_phone_number(phone_number):
    default_region = "ID"
    parsed_number = phonenumbers.parse(phone_number, default_region)
    region_code = phonenumbers.region_code_for_number(parsed_number)
    operator = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    time_zones = timezone.time_zones_for_number(parsed_number)
    number_type_description = phonenumbers.number_type(parsed_number)

    print(f"\n========== DETAILED INFORMATION PHONE NUMBERS ==========")
    print(f"Phone Number        : {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f"Location            : {location}")
    print(f"Region Code         : {region_code}")
    print(f"Operator            : {operator}")
    print(f"Number Type         : {number_type_description}")
    print(f"Time Zones          : {', '.join(time_zones)}")
    print(f"Valid               : {phonenumbers.is_valid_number(parsed_number)}")
    print(f"Possible            : {phonenumbers.is_possible_number(parsed_number)}")

def main():
    print_banner()

    while True:
        print("\n[1] IP Tracker")
        print("[2] Phone Tracker")
        print("[0] Exit")

        choice = input("\nPlease choose an option: ")

        if choice == "1":
            ip = input("\nEnter IP target: ")
            track_ip(ip)
        elif choice == "2":
            phone_number = input("\nEnter phone number target (Ex: +6281xxxxxxxxx): ")
            track_phone_number(phone_number)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
