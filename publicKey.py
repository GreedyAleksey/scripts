def publicEncrypt(message):
    public_key = (1249, 18949)
    encrypted_message = ""
    for char in message:
        encrypted_char = ord(char) ** public_key[0] % public_key[1]
        encrypted_message += '0' * (4 - len(hex(encrypted_char)[2:])) + hex(encrypted_char)[2:]

    return encrypted_message


def publicDecrypt(message):
    decrypted_message = ""
    private_key = (13, 18949)

    mass = []
    for i in range(0, len(message), 4):
        mass.append(message[i] + message[i + 1] + message[i + 2] + message[i + 3])

    for char in mass:
        decrypted_char = int(char, 16) ** private_key[0] % private_key[1]
        decrypted_message += chr(decrypted_char)

    return decrypted_message


if __name__ == '__main__':
    message = "Hello, World!"
    encryptMessage = publicEncrypt(message)
    print("Зашифрованное сообщение:", encryptMessage)

    decryptMessage = publicDecrypt(encryptMessage)
    print("Расшифрованное сообщение:", decryptMessage)
