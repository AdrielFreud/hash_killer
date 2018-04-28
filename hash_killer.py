#!/usr/bin/python

# Desenvolvido por Adriel Freud!
# Contato: businessc0rp2k17@gmail.com
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=
#conding: utf-8

import os
import sys
sys.path.append('libs')
import main
import crypt
import identify
import requests
import time, datetime

ts = time.time()
dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
today = datetime.datetime.today()
t = today.strftime("[%H:%M:%S] - ")

if 'win' in sys.platform:
	os.system('cls')
else:
	os.system('clear') 

def hash_killer(_hash, type_hash, wordlist):
	print(main.stack_menu())
	print("%s[==>] Trying to Break HASH!\nWaiting...\n"%t)
	main.head(wordlist, type_hash, _hash)

if len(sys.argv) < 3:
	if "identificar" in sys.argv[1]:
		identify.run()
	else:
		print(main.two_menu())
		crypt.fatal("Passe Parametros Suficientes!")

else:
	type_hash = sys.argv[1].lower()
	_hash = sys.argv[2]

	if _hash:
		if 'base64' in type_hash:
			print(main.stack_menu()+'\n%s[==>] Trying to break HASH!\nWaiting...\n'%t)
			crypt.base64decode(_hash)
			
		elif 'binary' in type_hash:
			print(main.stack_menu()+'\n%s[==>] Trying to break HASH!\nWaiting...\n'%t)
			crypt.binary(_hash)

		elif 'hex' in type_hash:
			print(main.stack_menu()+'\n%s[==>] Trying to break HASH!\nWaiting...\n'%t)
			crypt.hex(_hash)

		elif 'morse' in type_hash:
			print(main.stack_menu()+'\n%s[==>] Trying to break HASH!\nWaiting...\n'%t)
			crypt.morse(_hash)

		else:
			if sys.argv[3]:
				wordlist = sys.argv[3]
				hash_killer(_hash, type_hash, wordlist)
			else:
				crypt.fatal("Passe uma Wordlist como Parametro Final! :)")
	else:
		print(main.two_menu())
		crypt.fatal("Passe Parametros Suficientes!")


