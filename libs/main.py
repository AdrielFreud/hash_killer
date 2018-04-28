import crypt
import sys
import thread

menu = """
  _    _           _     _  ___ _ _           
 | |  | |         | |   | |/ (_) | |          
 | |__| | __ _ ___| |__ | ' / _| | | ___ _ __ 
 |  __  |/ _` / __| '_ \|  < | | | |/ _ \ '__|
 | |  | | (_| \__ \ | | | . \| | | |  __/ |   
 |_|  |_|\__,_|___/_| |_|_|\_\_|_|_|\___|_|

\tPowered by Adriel Freud...\n"""


menu_type = """
Modo de Uso: hash_killer.py MD5 "hashmd5" wordlist.txt
Para usar uma thread use: hash_killer.py thread
Caso Voce nao saiba o Tipo de sua Hash use: hash_killer.py identificar ou --identificar

[ 1 ] Morse  \t  - \t Hand Double
[ 2 ] Binary  \t  - \t Hand Double
[ 3 ] hexadecimal - \t Hand Double
[ 4 ] BASE64  \t  - \t Hand Double

[ 5 ] MD5 \t  - \t128 BITS
[ 6 ] SHA1 \t  - \t160 BITS
[ 7 ] SHA224 \t  - \t224 BITS
[ 8 ] SHA256 \t  - \t256 BITS
[ 9 ] SHA384 \t  - \t384 BITS
[ 10 ] SHA512     - \t512 BITS

[!] - This tool has a very effective hash-breaking method, using a thread, or its CPU itself, thus breaking more easily and quickly!\n
"""

def stack_menu():
	return menu

def stack_menu_type():
	return menu_type

def two_menu():
	return menu+menu_type

def head(wordlist, type_hash, _hash):
	try:
		with open(wordlist, 'r') as read:
			line = read.readlines()

			if 'md5' in type_hash.lower():
				crypt.MD5(_hash, line)
				sys.exit(0)

			elif 'sha1' in type_hash.lower():
					crypt.SHA1(_hash, line)
					sys.exit(0)

			elif 'sha224' in type_hash.lower():
					crypt.SHA224(_hash, line)
					sys.exit(0)

			elif 'sha256' in type_hash.lower():
					crypt.SHA256(_hash, line)
					sys.exit(0)

			elif 'sha384' in type_hash.lower():
					crypt.SHA384(_hash, line)
					sys.exit(0)

			elif 'sha512' in type_hash.lower():
					crypt.SHA512(_hash, line)
					sys.exit(0)
			else:
				crypt.fatal("Nenhuma das Opcoes e valida! Tente Novamente...")
	except:
		crypt.fatal("Caso o Programa nao Prosseguir reveja os Parametros passados e tente Novamente :)")
