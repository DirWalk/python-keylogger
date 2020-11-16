from cryptography.fernet import Fernet


def keygen():
    key = Fernet.generate_key()

    with open('mykey.key', 'wb') as mykey:
        mykey.write(key)


def run():
    keygen()


if __name__ == '__main__':
    run()
