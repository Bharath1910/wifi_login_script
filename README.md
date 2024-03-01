# Automate ~~the Boring Stuff with Python~~ wifi login

A python script to automate wifi login for VIT-AP's university and campus's wifi.

## Installation
1. `$ git clone https://github.com/Bharath1910/wifi_login_script.git`
2. `$ cd wifi_login_script`
3. `$ pip install -r requirements.txt`
4. `$ touch config.json`
5. Add the following to `config.json
	```json
	{
			"username": "your registration number",
			"password": "your wifi password",
			"hostel_endpoint": "https://hfw.vitap.ac.in:8090/login.xml",
			"campus_endpoint": ""
	}
	```
	> Note: The above endpoints are the default endpoints for the university and campus wifi. If the endpoints are changed, you can find the new endpoints by inspecting the network requests in the browser's developer tools.

## Usage
```
usage: main.py [-h] [-c C] [-i I] [-p] (--login | --logout)

A command line utility to login and logout from VITAP's hostel and campus wifi

options:
  -h, --help  show this help message and exit
  -c C        stop after <c> attempts to fetch wifi SSID (default is 4 attempts)
  -i I        change interval seconds between attempts (default is 5 seconds)
  -p          enable polling to fetch wifi SSID
  --login     attempt login
  --logout    attempt logout
```