#!/usr/bin/python3

#Import the libraries
try:
	import subprocess
	import time
	import requests
	from colorama import Fore
	from colorama import init as initializer
except ModuleNotFoundError:
	print(Fore.RED + '[-] Kindly Run requirements.txt before Running this setup.py')
	time.sleep(1)
	exit()

#Initializer

initializer(autoreset = True)

#Check Internet

def checkInternet() -> str :
	print(Fore.YELLOW + '\n\nChecking For Internet Connectivity ....\n')
	try:
		internetHit = requests.get('https://google.com/', timeout = 10)
		if internetHit.status_code == 200:
			return True
			time.sleep(1)
	except:
		return False

#Install DVWA and It's Dependencies

def installDVWAandDependencies():
	print(Fore.YELLOW + '[+] Installing DVWA\n')
	dvwa = subprocess.call('apt install dvwa -y', shell = True)
	time.sleep(1.5)
	print(Fore.GREEN + '\n[✓] DVWA Installed Sucessfully')
	time.sleep(1.8)
	print(Fore.YELLOW + '\n\n[+] Installing Dependecies...\n')
	dependecies = subprocess.call('apt install adduser apache2 libapache2-mod-php mariadb-server nginx php8.2 php8.2-fpm php8.2-gd php8.2-mysql sudo -y', shell = True)
	print(Fore.GREEN + '\n[✓] All Dependencies Installed Successfully')
	time.sleep(2.5)
	print(Fore.YELLOW + '\n[*] Launching The DVWA Environment...')
	time.sleep(1)
	lanuchEnvironment = subprocess.call('dvwa-start', shell = True)
	time.sleep(1)
	print(Fore. GREEN + '\n[✓] DVWA Vulnerable Enviromnent Installed Successfully.')

def mainDriver():
	checkInternet()
	if checkInternet:
		print(Fore.GREEN + '[✓] Connected To The Internet')
		installDVWAandDependencies()

	else:
		print(Fore.RED + '[✕] Error! Connecting To The Internet. Kindly Check YOur Internet Connection and Try Again.')
		exit()

mainDriver()
