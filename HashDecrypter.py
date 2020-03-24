from sys import argv
import hashlib

wordlist = open(argv[1], 'r').read().split('\n')

while '' in wordlist:
    wordlist.remove('')


hash_type = str(input('''
    [1] MD5
    [2] SHA1
    [3] SHA224
    [4] SHA256
    [5] SHA384
    [6] SHA512
'''))

while '123456' not in hash_type:
    print('Inválid Option! Try again...')
    hash_type = str(input('''
    [1] MD5
    [2] SHA1
    [3] SHA224
    [4] SHA256
    [5] SHA384
    [6] SHA512
--> '''))

hash_input = str(input('Insert the hash:'))

if hash_type == '1':
    for passwd in wordlist:
        hashed_passwd = hashlib.md5(passwd.encode()).hexdigest()

        if hash_input == hashed_passwd:
            print(f'FOUND --> {hashed_passwd}')
            break
if hash_type == '2':
    for passwd in wordlist:
        hashed_passwd = hashlib.sha1(passwd.encode()).hexdigest()

        if hash_input == hashed_passwd:
            print(f'FOUND --> {hashed_passwd}')
            break
if hash_type == '3':
    for passwd in wordlist:
        hashed_passwd = hashlib.sha224(passwd.encode()).hexdigest()

        if hash_input == hashed_passwd:
            print(f'FOUND --> {hashed_passwd}')
            break

if hash_type == '4':
    for passwd in wordlist:
        hashed_passwd = hashlib.sha256(passwd.encode()).hexdigest()

        if hash_input == hashed_passwd:
            print(f'FOUND --> {hashed_passwd}')
            break
if hash_type == '5':
    for passwd in wordlist:
        hashed_passwd = hashlib.sha384(passwd.encode()).hexdigest()

        if hash_input == hashed_passwd:
            print(f'FOUND --> {hashed_passwd}')
            break
if hash_type == '6':
    for passwd in wordlist:
        hashed_passwd = hashlib.sha512(passwd.encode()).hexdigest()

        if hash_input == hashed_passwd:
            print(f'FOUND --> {hashed_passwd}')
            break
