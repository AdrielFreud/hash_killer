import hashlib
import os
import sys
import base64
from time import sleep
import string
import time, datetime

ts = time.time()
dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
today = datetime.datetime.today()
t = today.strftime("[%H:%M:%S] - ")

morseAlphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "=": "-...-"
}

def fatal(msg):
	sys.stdout.write('[WARNING] - %s\n'%msg)
	sys.exit(0)

inverseMorseAlphabet = dict((v, k) for (k, v) in morseAlphabet.items())

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def decodeMorse(message):
    messageSeparated = message.split(' ')
    decodeMessage = ''
    for char in messageSeparated:
        if char in inverseMorseAlphabet:
            decodeMessage += inverseMorseAlphabet[char]
        else:
            decodeMessage += '<CNF>'
    return decodeMessage

def base64decode(hash):
	real_hash = hash.strip()
	hash_decrypted = base64.b64decode(real_hash)
	print("%s[=>] Text: -> %s"%(t, hash_decrypted))
	print("%s[=>] Real Hash -> %s\n"%(t, hash))

def binary(hash):
	print("%s[=>] Text: -> %s"%(t, decode_binary_string(hash)))
	print("%s[=>] Real Hash -> %s\n"%(t, hash))

def hex(hash):
	print("%s[=>] Text: -> %s"%(t, hash.decode('hex')))
	print("%s[=>] Real Hash -> %s\n"%(t, hash))

def morse(hash):
	print("%s[=>] Text: -> %s"%(t, decodeMorse(hash)))
	print("%s[=>] Real Hash -> %s\n"%(t, hash))

def MD5(hash, line):
	for lines in line:
		encrypt = hashlib.md5(lines.strip()).hexdigest()
		if encrypt == hash:
			print("%s[=>] Hash Cracked -> %s"%(t, lines))
			print("%s[=>] Real Hash -> %s\n"%(t, encrypt))

	fatal("Impossivel Quebrar Hash, Tente novamente com Outra Wordlist!")

def SHA1(hash, line):
	for lines in line:
		encrypt = hashlib.sha1(lines.strip()).hexdigest()
		if encrypt == hash:
			print("%s[=>] Hash Quebrada -> %s"%(t, lines))
			print("%s[=>] Real Hash -> %s\n"%(t, encrypt))

	fatal("Impossivel Quebrar Hash, Tente novamente com Outra Wordlist!")

def SHA224(hash, line):
	for lines in line:
		encrypt = hashlib.sha224(lines.strip()).hexdigest()
		if encrypt == hash:
			print("%s[=>] Hash Quebrada -> %s"%(t, lines))
			print("%s[=>] Real Hash -> %s\n"%(t, encrypt))

	fatal("Impossivel Quebrar Hash, Tente novamente com Outra Wordlist!")

def SHA256(hash, line):
	for lines in line:
		encrypt = hashlib.sha256(lines.strip()).hexdigest()
		if encrypt == hash:
			print("%s[=>] Hash Quebrada -> %s"%(t, lines))
			print("%s[=>] Real Hash -> %s\n"%(t, encrypt))
			sys.exit(0)

	fatal("Impossivel Quebrar Hash, Tente novamente com Outra Wordlist!")

def SHA384(hash, line):
	for lines in line:
		encrypt = hashlib.sha384(lines.strip()).hexdigest()
		if encrypt == hash:
			print("%s[=>] Hash Quebrada -> %s"%(t, lines))
			print("%s[=>] Real Hash -> %s\n"%(t, encrypt))

	fatal("Impossivel Quebrar Hash, Tente novamente com Outra Wordlist!")

def SHA512(hash, line):
	for lines in line:
		encrypt = hashlib.sha512(lines.strip()).hexdigest()
		if encrypt == hash:
			print("%s[=>] Hash Quebrada -> %s"%(t, lines))
			print("%s[=>] Real Hash -> %s\n"%(t, encrypt))

	fatal("Impossivel Quebrar Hash, Tente novamente com Outra Wordlist!")

def RIPEMD160(hash, line):
	for lines in line:
		encrypt = hashlib.new('ripemd160', lines.strip()).hexdigest()
		if encrypt == hash:
			print("%s[=>] Hash Quebrada -> %s"%(t, lines))
			print("%s[=>] Real Hash -> %s\n"%(t, encrypt))

	fatal("Impossivel Quebrar Hash, Tente novamente com Outra Wordlist!")
