import sys
import base64
from Crypto.Cipher import AES

def extract_payload_version(var):
    result = var.split('=')
    return (int(result[1].strip())+1)


def check(filename):
    # Your solution.
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line.strip())
            
    if(len(lines) < 3):
        #for only payload files    
        return extract_payload_version(lines[0])
    elif (len(lines) > 2):
        code_locals = {}
        for i in range(7):
            exec(lines[i], globals(), code_locals)
            
        payload = code_locals['c2'].strip().split('\n')
        return extract_payload_version(payload[0])
    else:
        return None
    

if __name__ == '__main__':
    check(sys.argv[1])
