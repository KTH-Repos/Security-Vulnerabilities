import sys
import base64
from Crypto.Cipher import AES

def extract(var):
    if "=" in var:
        result = var.split('=')
        return (int(result[1].strip())+1)
    return None
    

def check(filename):
    # Your solution.
    lines = []
    with open(filename, "r") as file:
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line:
                lines.append(cleaned_line) 

    if "1" in lines[0] or "0" in lines[0]:
        return extract(lines[0])
    else:
        if "c1" in lines[3]:
            code_locals = {}
            for i in range(7):
                exec(lines[i], globals(), code_locals)
            payload = code_locals['c2'].strip().split('\n')
            return extract(payload[0])
        return None
   


if __name__ == '__main__':
    check(sys.argv[1])
