# Automate ~~the Boring Stuff with Python~~ wifi login

A python script to automate wifi login for VIT-AP's hostel and campus's wifi.

## Installation

> **Note:** if you are going to copy paste the commands, dont copy the `$` symbol, it is just a convention. (Have to include these nowadays)

1. `Clone the repository`
2. `$ cd wifi_login_script`
3. `$ touch config.json` (if you are on windows and this command shows scary red text, just right click and create a new file and name it `config.json`.)
5. Add the following to `config.json`
	```json
	{
		"username": "your registration number",
		"password": "your wifi password",
		"hostel_endpoint": "https://hfw.vitap.ac.in:8090/login.xml",
		"campus_endpoint": ""
	}
	```
	> **Note:** The above endpoints are the default endpoints for the hostel and campus wifi. If the endpoints are changed, you ~~should be smart enough to figure it out~~ can find the new endpoints by inspecting the network requests in the browser's developer tools.

## Usage
```
usage: main.py [-h] (--login | --logout)

A command line utility to login and logout from VITAP's campus wifi

options:
  -h, --help  show this help message and exit
  --login     attempt login
  --logout    attempt logout
```

## Examples
```bash
$ python3 campus_wifi.py
$ python3 campus_wifi.py --login #Directly log in to your account
$ python3 campus_wifi.py --logout #Directly log out of your account
```