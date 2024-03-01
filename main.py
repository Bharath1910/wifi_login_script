import requests
import json
from typing import TypedDict
from abc import ABC, abstractmethod
from datetime import datetime
import subprocess
import time
import argparse
from enum import Enum

class Wifi(Enum):
    HOSTEL = "VITAP-HOSTEL"
    CAMPUS = "VIT-AP"
    UNKNOWN = "UNKNOWN"
class Config(TypedDict):
    username: str
    password: str
    hostel_endpoint: str
    campus_endpoint: str
    # TODO: Add on success and failure runners
    # on_success: list[str]
    # on_failure: list[str]

# I really have to come up with a better name than Base :/
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

class Hostel(Base):        
    def login(self) -> None:
        url = self.config['hostel_endpoint']
        headers = Hostel.generate_headers()
        data = {
            "mode": "191",
            "username": self.config['username'],
            "password": self.config['password'],
            "a": str(int(datetime.now().timestamp()))
        }

        response = requests.post(url, headers=headers, data=data, verify=False)
        print(response.status_code)
        print(response.text)


    def logout(self) -> None:
        url = self.config['hostel_endpoint']
        headers = Hostel.generate_headers()
        data = {
            "mode": "193",
            "username": self.config['username'],
            "a": str(int(datetime.now().timestamp()))
        }

        response = requests.post(url, headers=headers, data=data, verify=False)
        print(response.status_code)
        print(response.text)

    @staticmethod
    def generate_headers() -> dict:
        # Too lazy to only include required headers
        return {
            "Host": "hfw.vitap.ac.in:8090",
            "Content-Length": "75",
            "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120"',
            "Sec-Ch-Ua-Platform": "Linux",
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Origin": "https://hfw.vitap.ac.in:8090",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://hfw.vitap.ac.in:8090/httpclient.html",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Priority": "u=1, i",
            "Connection": "close"
        }

class Campus(Base):
    @staticmethod
    def fetch_magic() -> str:
        pass

def parse_args() -> dict:
    ap = argparse.ArgumentParser(description="A command line utility to login and logout from VITAP's hostel and campus wifi")
    ap.add_argument("-c", help="stop after <c> attempts to fetch wifi SSID (default is 4 attempts)")
    ap.add_argument("-i", help="change interval seconds between attempts (default is 5 seconds)")
    ap.add_argument("-p", action="store_true", help="enable polling to fetch wifi SSID")

    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--login", action="store_true", help="attempt login")
    group.add_argument("--logout", action="store_true", help="attempt logout")
    
    return vars(ap.parse_args())

def fetch_ssid(args: dict, poll: bool = False) -> Wifi:
    if not poll:
        if 'VITAP-HOSTEL' in str(subprocess.check_output("iwgetid")):
            return Wifi.HOSTEL

        elif 'VIT-AP' in str(subprocess.check_output("iwgetid")):
            return Wifi.CAMPUS

        else:
            return Wifi.UNKNOWN

    if args['c'] is None:
        args['c'] = 4

    if args['i'] is None:
        args['i'] = 5

    for _ in range(int(args['c'])):
        if 'VITAP-HOSTEL' in str(subprocess.check_output("iwgetid")):
            return Wifi.HOSTEL

        elif 'VIT-AP' in str(subprocess.check_output("iwgetid")):
            return Wifi.CAMPUS

        time.sleep(int(args['i']))

def attempt_login(args: dict, wifi: Wifi) -> None:
    if wifi == Wifi.HOSTEL:
        hostel = Hostel()
        hostel.login()

    elif wifi == Wifi.CAMPUS:
        campus = Campus()
        campus.login()

    else:
        print("Unknown wifi")

def attempt_logout(args: dict, wifi: Wifi) -> None:
    if wifi == Wifi.HOSTEL:
        hostel = Hostel()
        hostel.logout()

    elif wifi == Wifi.CAMPUS:
        campus = Campus()
        campus.logout()

    else:
        print("Unknown wifi")

def main() -> None:
    if '"VITAP-HOSTEL"' in str(subprocess.check_output("iwgetid")):
        hostel = Hostel()
        print("Connected to VITAP-HOSTEL")
        res = requests.get("http://connectivitycheck.gstatic.com/generate_204")
        if res.status_code != 204:
            hostel.login()

if __name__ == "__main__":
    main()