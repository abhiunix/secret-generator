#!/usr/bin/python3.7

import secrets
import string
import sys
import os
from colorama import Fore,Style


def banner():
	os.system("clear")
	os.system("pyfiglet 'Secret Generator'")
	print( Style.BRIGHT + Fore.WHITE + """                                                    
             """ + Style.DIM + Fore.BLUE + "\t\t@abhiunix\n\n")
banner()

Secretkey = ""
for i in range(int(str(sys.argv[1]))):
	secretX= print(Secretkey.join(secrets.choice(string.digits + string.ascii_letters + string.punctuation)), end='')
print("Secret is: " + str(secretX))