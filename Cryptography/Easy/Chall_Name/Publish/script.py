#!/usr/bin/python3

from base64 import b64encode, b32encode
from flag import FLAG

ct = b32encode(FLAG)
ct = b64encode(ct)

print(ct)

