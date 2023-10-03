#!/usr/bin/python3

from base64 import b64decode, b32decode

f = open('../Publish/out.txt','rb')

ct = f.read().strip()

ct = b64decode(ct)
ct = b32decode(ct)

print(ct)
