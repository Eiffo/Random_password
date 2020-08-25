import random
import string
from time import sleep


def random_password():
    length = input()
    letters = string.ascii_letters
    password = "".join(random.choice(letters) for i in range(int(length)))
    print("Your password is: {}".format(password))


while True:
    print("\nHow long password need to be: ")
    random_password()
    print('\nIf you want to end this, write: "stop"')
    print('if you want another password write: "next"')
    what = input()
    if what == "stop":
        break
    elif what == "next":
        continue
    else:
        print("There is no options")
        sleep(2)
        break
