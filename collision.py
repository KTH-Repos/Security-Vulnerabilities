#!/usr/bin/env python3
from insecure_hash import hash_string
from Crypto.Cipher import AES


def find_collision(message):
    # Your solution.
    string = b'asdfghjklzxcvbnm'
    message_hashed = hash_string(message)
    cipher = AES.new(string)
    collision_string = cipher.encrypt(message_hashed)
    return collision_string + string


if __name__ == '__main__':
    message = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb".encode()
    print("Hash of %s is %s" % (message, hash_string(message)))
    collision = find_collision(message)
    print("Hash of %s is %s" % (collision, hash_string(collision)))
