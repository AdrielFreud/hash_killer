## AdrielFreud

![](https://img.shields.io/badge/hash_killer-v2.0-blue?style=flat&logo=appveyor)
![](https://img.shields.io/badge/plataforma-win32--win64--linux64--linux32-blue?style=flat&logo=appveyor)
![](https://img.shields.io/badge/python-3.x.x-blue)

 - O Script tem a dependencia de uma wordlist,
 - Onde ele possa fazer as verificações, até encontrar a chave combinatoria.
 - Modo CPU para agilizar a quebra.
 
 ```python
for lines in line:
	encrypt = hashlib.TYPECRYPT(lines.strip()).hexdigest()
	if encrypt == hash:
		...success
```

## AVISO
- Caso você tenha uma sugestão de código [Click-aqui](https://github.com/AdrielFreud/hash_killer/issues/new) crie uma issue.

## Imagem
![photo](https://i.imgur.com/Zk9OYBL.png)

## Características
  - Quebra de hash.
  - Aplicação para Forense Computacional.
 
 ## Download
Baixe diretamente do github com:
 - git clone https://github.com/AdrielFreud/hash_killer.git
 - ou https://github.com/AdrielFreud/hash_killer/archive/master.zip


## Uso
 - py hash_killer.py [type_hash] "hash"

## Requerimentos
 - Python3
