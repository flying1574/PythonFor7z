#-*- coding: UTF-8 -*-

import os

rar_path = "Package.7z" # The package.7z is Encrypted package Name 
with open('Passwords.txt') as pswd:   #Password.txt is Encrypted package Password dictionary
    pw = pswd.readlines()
for ps in pw:
    cmd = '7z.exe x "{}" -p{}'.format(rar_path,ps)
    os.system(cmd)
