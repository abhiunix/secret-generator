import secrets
import string
import sys

Secretkey = ""
for i in range(int(str(sys.argv[1]))):
	print(Secretkey.join(secrets.choice(string.digits + string.ascii_letters + string.punctuation)), end='')
