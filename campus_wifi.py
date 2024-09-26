#!/home/mystichqra/Documents/Projects/wifi_login_script/.venv/bin/python

import requests
import json
from typing import TypedDict
from abc import ABC, abstractmethod
import subprocess
import re
import csv
import argparse

class Config(TypedDict):
    username: str
    password: str
    hostel_endpoint: str
    campus_endpoint: str

class Base(ABC):
    def __init__(self) -> None:
        # TODO: Implement exception handling
        self.config: Config = json.load(open("./config.json", "r"))
    
    @abstractmethod
    def login(self) -> None:
        pass

    @abstractmethod
    def logout(self) -> None:
        pass

    @abstractmethod
    def generate_headers() -> dict:
        pass

class Campus(Base):
    def fetch_magic(self) -> str:
        url = self.config["campus_endpoint"]

        try:
            html = subprocess.run(
                ["wget", "--no-check-certificate", "-O-", f"{url}/login?"], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running wget: {e}")
            print(f"stderr: {e.stderr.decode('utf-8')}")
            return None

        magicRegex = re.compile(r'<input type="hidden" name="magic" value="([^"]+)">')
        match = magicRegex.search(str(html.stdout))

        if match:
            return match.group(1)
        else:
            raise ValueError("Magic token not found in the HTML response.")

    def login(self) -> None:
        magic = self.fetch_magic()
        url = self.config["campus_endpoint"]
        file = open('wifi.csv', mode='r')
        creds = list(csv.reader(file))
        #print(creds_copy)
        for cred in creds:
            res = requests.post(url, data={
                "4Tredir": "https://172.18.10.10:1000/login?",
                "magic": magic,
                "username": cred[0],
                "password": cred[1]
            }, verify=False)
            #print(res.text)

            if "https://172.18.10.10:1000/keepalive?" in res.text:
                print(f"Login Successful using {cred}")
                break
            elif "Sorry, user&apos;s concurrent authentication is over limit" in res.text:
                print(f"Concurrent Login while using {cred}")
                continue
            else:
                print(f"Invalid login while using {cred}")
                continue
        else:
            print("Reached end of the csv file")


    def logout(self) -> None:
        url = self.config["campus_endpoint"]
        html = subprocess.run(
                ["wget", "--no-check-certificate", "-O-", f"{url}/logout?"], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                check=True
        )
        html_content = html.stdout.decode('utf-8')
        #print(html_content)

        if "You have successfully logged out" in html_content:
            print("Logout Successful")

    def generate_headers() -> dict:
        pass

def parse_args() -> dict:
    ap = argparse.ArgumentParser(description="A command line utility to login and logout from VITAP's hostel and campus wifi")
    ap.add_argument("-c", help="stop after <c> attempts to fetch wifi SSID (default is 4 attempts)")
    ap.add_argument("-i", help="change interval seconds between attempts (default is 5 seconds)")
    ap.add_argument("-p", action="store_true", help="enable polling to fetch wifi SSID")

    group = ap.add_mutually_exclusive_group(required=False)
    group.add_argument("--login", action="store_true", help="attempt login")
    group.add_argument("--logout", action="store_true", help="attempt logout")
    
    return vars(ap.parse_args())

def main() -> None:
    
    args = parse_args()
    campus = Campus()

    if args['login']:
        campus.login()
    elif args['logout']:
        campus.logout()
    else:
        print("Campus Automated Wifi Login")
        print("1. Login")
        print("2. Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            campus.login()
        elif choice == 2:
            campus.logout()
        else:
            print("arigato <3")

if __name__ == "__main__":
    main()