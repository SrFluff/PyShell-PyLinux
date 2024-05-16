import os

def cls():

    os.sytem('clear')

runtime = 1

start = 1

lock = 0

lockfail = 0

password = ""

while runtime:

    while start:

        cls()

        print("PyShell lite\n")

        print("b - boot")
        print("s - settings")
        print("p - set password")
        print("l - lock")
        print("q - quit\n")

        a = input("> ")

        if a == "q":

            cls()

            quit()

        if a == "l":

            if password != "":

                start = 0

                lock = 1

            else:

                start = 0

                lockfail = 1

    while lock:

        cls()

        print("PyShell lite\n")

        print("a - enter password")
        print("q - quit\n")

        a = input("> ")

        if a == "a":

            cls()

            print("PyShell lite\n")

            print("Enter the password\n")

            a = input("> ")

            if a == password:

                lock = 0

                start = 1

            else:

                cls()

                lock = 1