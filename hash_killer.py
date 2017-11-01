#!/usr/bin/python

# Desenvolvido por Adriel Freud!
# Contato: usuariocargo2016@gmail.com 
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=

import hashlib
import requests
import os
import sys
import base64

if 'win' in sys.platform:
	os.system('cls')
else:
	os.system('clear') 

menu = """
  _    _           _     _  ___ _ _           
 | |  | |         | |   | |/ (_) | |          
 | |__| | __ _ ___| |__ | ' / _| | | ___ _ __ 
 |  __  |/ _` / __| '_ \|  < | | | |/ _ \ '__|
 | |  | | (_| \__ \ | | | . \| | | |  __/ |   
 |_|  |_|\__,_|___/_| |_|_|\_\_|_|_|\___|_|

\tPowered by Adriel Freud...\n"""

menu_type = """
Modo de Uso: hash_killer.py MD5 hashmd5 wordlist.txt

[ 1 ] MD5 - \t128 BITS
[ 2 ] BASE64 - \tHand double
[ 3 ] SHA1 - \t160 BITS
[ 4 ] SHA224 - \t224 BITS
[ 5 ] SHA256 - \t256 BITS
[ 6 ] SHA384 - \t384 BITS
[ 7 ] SHA512 - \t512 BITS
"""

def fatal(msg):
	sys.stdout.write('[WARNING] - %s\n'%msg)
	sys.exit(0)

def hash_killer(hash, type_hash, wordlist):
	print(menu)
	print("[==>] Trying to Break HASH!\nWaiting...\n")

	with open(wordlist, 'r') as read:
		line = read.readlines()
		if 'md5' in type_hash.lower():
			for lines in line:
				encrypt = hashlib.md5(lines.strip()).hexdigest()
				if encrypt == hash:
					print("[=>] Hash Cracked -> %s"%lines)
					print("[=>] Real Hash -> %s\n"%encrypt)
					sys.exit(0)

			fatal("Impossivel Quebrar Hash, Tente novamente com Outra Wordlist!")

		elif 'sha1' in type_hash.lower():
			for lines in line:
				encrypt = hashlib.sha1(lines.strip()).hexdigest()
				if encrypt == hash:
					print("[=>] Hash Quebrada -> %s"%lines)
					print("[=>] Real Hash -> %s\n"%encrypt)
					sys.exit(0)

			fatal("Impossivel Quebrar Hash, Tente novamente com Outra Wordlist!")

		elif 'sha224' in type_hash.lower():
			for lines in line:
				encrypt = hashlib.sha224(lines.strip()).hexdigest()
				if encrypt == hash:
					print("[=>] Hash Quebrada -> %s"%lines)
					print("[=>] Real Hash -> %s\n"%encrypt)
					sys.exit(0)

			fatal("Impossivel Quebrar Hash, Tente novamente com Outra Wordlist!")

		elif 'sha256' in type_hash.lower():
			for lines in line:
				encrypt = hashlib.sha256(lines.strip()).hexdigest()
				if encrypt == hash:
					print("[=>] Hash Quebrada -> %s"%lines)
					print("[=>] Real Hash -> %s\n"%encrypt)
					sys.exit(0)

			fatal("Impossivel Quebrar Hash, Tente novamente com Outra Wordlist!")

		elif 'sha384' in type_hash.lower():
			for lines in line:
				encrypt = hashlib.sha384(lines.strip()).hexdigest()
				if encrypt == hash:
					print("[=>] Hash Quebrada -> %s"%lines)
					print("[=>] Real Hash -> %s\n"%encrypt)
					sys.exit(0)

			fatal("Impossivel Quebrar Hash, Tente novamente com Outra Wordlist!")

		elif 'sha512' in type_hash.lower():
			for lines in line:
				encrypt = hashlib.sha512(lines.strip()).hexdigest()
				if encrypt == hash:
					print("[=>] Hash Quebrada -> %s"%lines)
					print("[=>] Real Hash -> %s\n"%encrypt)
					sys.exit(0)

			fatal("Impossivel Quebrar Hash, Tente novamente com Outra Wordlist!")

		else:
			fatal("Nenhuma das Opcoes e valida! Tente Novamente...")


if len(sys.argv) < 2:
	print(menu+menu_type)
	fatal("Passe Parametros Suficientes!")
else:
	type_hash = sys.argv[1]
	hash = sys.argv[2]
	if 'base64' in type_hash.lower():
		print(menu+'\n[==>] Trying to break HASH!\nWaiting...\n')
		hash_decrypted = base64.b64decode(hash)
		print("[=>] Hash Quebrada -> %s"%hash_decrypted)
		print("[=>] Real Hash -> %s\n"%hash)
	else:
		if sys.argv[3]:
			wordlist = sys.argv[3]
			hash_killer(hash, type_hash, wordlist)

		print(menu+'\n[+] Passe uma wordlist como ultimo parametro!')
