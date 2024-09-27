# VIT-AP Campus Wifi Automation
## (~~Automate the Boring Stuff with Python~~)

A python script to automate the wifi login for VIT-AP's campus's wifi.

## Features
1. Automate the wifi login and logout by setting your credentials in the config.json.
2. Automate the same for a list of credentials by using a csv file (wifi.csv).

## Requirements
- python 3.x (duh)

## Installation

> **Note:** if you are going to copy paste the commands, dont copy the `$` symbol, it is just a convention. (Have to include these nowadays)

1. Clone this repository.
2. `$ cd wifi_login_script`

## Usage
```
campus_wifi.py [-h] (--login | --logout)
campus_wifi_csv.py [-h] (--login | --logout)

A command line utility to login and logout from VITAP's campus wifi

options:
  -h, --help  show this help message and exit
  --login     attempt login
  --logout    attempt logout
```

## Examples

> **Note:** If you're on linux, you might want to use `python3` instead of `python` in these examples.

```bash
$ python campus_wifi.py
$ python campus_wifi.py --login #Directly log in to your account
$ python campus_wifi.py --logout #Directly log out of your account

$ python campus_wifi_csv.py
$ python campus_wifi_csv.py --login #Directly log in to an account from the csv
$ python campus_wifi_csv.py --logout #Directly log out of an account from the csv
```
## Help Section
**If you use campus_wifi.py for logging in, then you need to set your username and password in the config.json file.**
> **Note:** The endpoints defined in the config.json file are the default endpoints for the hostel and campus wifi. If the endpoints are changed, you ~~should be smart enough to figure it out~~ can find the new endpoints by inspecting the network requests in the browser's developer tools.

**If you use the campus_wifi_csv.py for logging in, then you need to create a wifi.csv file containing the credentials that you want the script to use for logging in.**

## Example for wifi.csv file:
```
username1, password1
username2, password2
username3, password3
```