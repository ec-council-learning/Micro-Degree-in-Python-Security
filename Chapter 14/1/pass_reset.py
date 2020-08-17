# user1 : Start!123
# user2 : Admin!123
import ctypes
import os
import hashlib
import json
from getpass import getpass

if os.name == 'nt':
    checker = ctypes.windll.shell32.IsUserAnAdmin
else:
    checker = os.getuid

if checker() == 0:
    raise SystemExit("This script must be ran as Administrator!")
else:
    print("The Administrators get a free pass!")

with open("pass.db","r") as passdb:
    UserDataBase =  dict(json.load(passdb))

class Hasher(object):
    @classmethod
    def get_hex(self, value):
        self.hasher = hashlib.sha256()
        self.hasher.update(bytes(value,'utf-8'))
        return self.hasher.hexdigest()

def check_user(user):
    return Hasher.get_hex(user) in UserDataBase

def check_old_pass(user, password):
    userdigest = Hasher.get_hex(user)
    passdigest = Hasher.get_hex(password)
    return UserDataBase.get(userdigest) == passdigest

def update_password(user, password):
    userdigest = Hasher.get_hex(user)
    passdigest = Hasher.get_hex(password)
    UserDataBase[userdigest] = passdigest
    with open("pass.db","w") as passdb:
        json.dump(UserDataBase, passdb)

while True:
    UserToReset = input("Give me the user to reset the password: ")
    if check_user(UserToReset):
        break
    else:
        print("You have specified an invalid user!")

OldPassword = getpass("Give me the current password: ")
if check_old_pass(UserToReset, OldPassword):
    pass
else:
    raise SystemExit("The current password for the user is invalid!")

while True:
    first = getpass("Give me the new password: ")
    second = getpass("Give me the new password again: ")
    if first != second:
        print("The passwords do not match!")
    else:
        if not check_old_pass(UserToReset, first):
            print("The password was reset!")
            update_password(UserToReset, first)
            break
        else:
            print("THe old and new password must be different!")
