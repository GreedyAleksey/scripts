from publicKey import *

def readF(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = (lines[i])[:-1]

    return lines

def writeF(file, mass, status):
    if status == 'old':
        with open(file, 'w') as f:
            for i in range(len(mass)):
                f.write(mass[i]+'\n')

    if status == 'new':
        with open(f'{file[:-4]}Encrypt.txt', 'w') as f:
            for i in range(len(mass)):
                f.write(mass[i]+'\n')

def encryptMass(file, script):
    text = readF(file)

    if script == 'publicKey':
        for i in range(len(text)):
            text[i] = publicEncrypt(text[i])

    if script == 'something':
        pass

    return text

def decryptMass(file, script):
    text = readF(file)

    if script == 'publicKey':
        for i in range(len(text)):
            text[i] = publicDecrypt(text[i])

    if script == 'something':
        pass

    return text
