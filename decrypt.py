from cryptography.fernet import Fernet


def decrypt():
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()

    with open('keylogger.enc', 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = key.decrypted(encrypted)

    with open('keylogger.txt', 'wb') as dec_file:
        dec_file.write(decrypted)


def run():
    decrypt()


if __name__ == '__main__':
    run()
