# Automate ~~the Boring Stuff with Python~~ wifi login

A python script to automate wifi login for VIT-AP's hostel and campus's wifi.

## Installation
I recommend using a [venv](https://docs.python.org/3/library/venv.html) so that this project's dependencies wont mess up your system wide dependencies.
The below steps assumes you are using linux or mac, if you are using windows, the commands should work as long as you have git, python and pip installed.

> **Note:** if you are going to copy paste the commands, dont copy the `$` symbol, it is just a convention. (Have to include these nowadays)

1. `$ git clone https://github.com/Bharath1910/wifi_login_script.git`
2. `$ cd wifi_login_script`
3. `$ pip install -r requirements.txt`
4. `$ touch config.json` (if you are on windows and this command shows scary red text, just right click and create a new file and name it `config.json`.)
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

## Examples
```bash
$ python3 main.py --login
$ python3 main.py --logout
$ python3 main.py --login -p -c 10 -i 10 # enables polling, stops after 10 attempts and changes interval to 10 seconds
```