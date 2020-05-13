#-*- coding: UTF-8 -*-

import os

rar_path = "server.7z"
with open('Decode.txt') as pswd:
    pw = pswd.readlines()
for ps in pw:
    cmd = '7z.exe x "{}" -p{}'.format(rar_path,ps)
    print(cmd)
#    os.system(cmd)
