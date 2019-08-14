## AdrielFreud

![](https://img.shields.io/badge/hash_killer-v2.0-blue?style=flat&logo=appveyor)
![](https://img.shields.io/badge/plataforma-win32--win64--linux64--linux32-blue?style=flat&logo=appveyor)
![](https://img.shields.io/badge/python-3.x.x-blue)

 - O Script tem a Dependencia de uma wordlist onde ele faz a varredura,
 - Assim fazendo a verificação de linha por linha, até encontrar a chave que casa com a outra encriptografada.
 - Modo CPU para forçar a quebra.
 
 ```python
for lines in line:
	encrypt = hashlib.TYPECRYPT(lines.strip()).hexdigest()
	if encrypt == hash:
		...success
```

## AVISO
- Caso você encontrar um bug [Click-aqui](https://github.com/AdrielFreud/hash_killer/issues/new) e crie um issue para eu corrijir o bug.

## Imagem
![photo](https://i.imgur.com/Zk9OYBL.png)

## Características
  - Quebra de hash.
  - Aplicação para Forense Computacional.
 
 ## Dowloand
Baixe diretamente do github com:
 - git clone https://github.com/AdrielFreud/hash_killer.git
 - ou https://github.com/AdrielFreud/hash_killer/archive/master.zip


## Uso
 - py hash_killer.py [type_hash] "hash"

## Requerimentos
 - Python3
# Bibliotecas python necessarias:
  - pip install requests
