import os


def cls():
    os.system('clear')


main = 1

welcome = 1

setup = 0

info = 0

exit = 0

name = "admin"

password = ""

home = 0

filem = 0

sysi = 0

lock = 0

cmd = 0

shutdown = 0

c = 0

users = 0

drivers = 0

pydos = 0

programfiles = 0

system32 = 0

admin = 0

cls()

while main:
    
    while welcome:

        cls()

        print("[ Welcome to PyDos   ]")
        print("+--------------------+")
        print("|                    |")
        print("| [1] Setup          |")
        print("| [2] Info           |")
        print("| [3] Exit           |")
        print("|                    |")
        print("+--------------------+\n")

        a = input("> ")

        if a == "3":

            welcome = 0

            exit = 1

        if a == "2":

            welcome = 0

            info = 1

    while exit:

        cls()

        print("[ Exit               ]")
        print("+--------------------+")
        print("|                    |")
        print("| Are you sure?      |")
        print("|                    |")
        print("| [1] Yes            |")
        print("| [2] No             |")
        print("|                    |")
        print("+--------------------+\n")

        a = input("> ")

        if a == "1":

            cls()

            quit()

        if a == "2":

            exit = 0

            welcome = 1

        if a == "1":

            welcome = 0

            setup = 1

    while info:

        cls()

        print("[ Info               ]")
        print("+--------------------+")
        print("|                    |")
        print("| PyDos is an ascii- |")
        print("| window  based OS.  |")
        print("| the name is based  |")
        print("| off of DOS by      |")
        print("| Microsoft. Made by |")
        print("| Franco M. with     |")
        print("| Python in Visual   |")
        print("| Studio Code by     |")
        print("| Microsoft.         |")
        print("|                    |")
        print("| [1] Go back        |")
        print("|                    |")
        print("+--------------------+\n")

        a = input("> ")

        if a == "1":

            info = 0

            welcome = 1

    while setup:

        cls()

        print("[ Setup              ]")
        print("+--------------------+")
        print("|                    |")
        print("| First, choose your |")
        print("| user name.         |")
        print("|                    |")
        print("+--------------------+\n")

        name = input("Username: ")

        cls()

        print("[ Setup              ]")
        print("+--------------------+")
        print("|                    |")
        print("| Now, choose a safe |")
        print("| password           |")
        print("|                    |")
        print("+--------------------+\n")

        password = input("Password: ")

        cls()

        setup = 0

        home = 1

    while home:

        cls()

        print("[ PyDos              ]")
        print("+--------------------+")
        print("|                    |")
        print("| [1] File manager   |")
        print("| [2] System info    |")
        print("| [3] Lock PC        |")
        print("| [4] Command line   |")
        print("| [5] Shutdown       |")
        print("|                    |")
        print("+--------------------+\n")

        a = input(name + "/> ")

        if a == "1":

            home = 0

            filem = 1

    while filem:

        cls()

        print("[ File manager       ]")
        print("+--------------------+")
        print("|                    |")
        print("| [1] c:\            |")
        print("|                    |")
        print("+--------------------+\n")

        a = input(name + "/> ")

        if a == "1":

            c = 1

            filem = 0

    while c:

        cls()

        print("[ c:\                ]")
        print("+--------------------+")
        print("|                    |")
        print("| [1] users          |")
        print("| [2] drivers        |")
        print("| [3] pydos          |")
        print("| [4] system32       |")
        print("| [5] program files  |")
        print("| [6] Go back        |")
        print("|                    |")
        print("+--------------------+\n")

        a = input(name + "/> ")

        if a == "1":

            c = 0

            users = 1

        if a == "2":

            c = 0

            drivers = 1

        if a == "3":

            c = 0

            pydos = 1

        if a == "4":

            c = 0

            system32 = 1

        if a == "5":

            c = 0

            programfiles = 1

        if a == "6":

            c = 0

            filem = 1

    while users:

        cls()

        print("[ c:\users\             ]")
        print("+--------------------+")
        print("|                    |")
        print("| [1] admin(you)     |")
        print("| [2] Go back        |")
        print("|                    |")
        print("+--------------------+\n")

        if a == "1":

            users = 0

            admin = 1

        if a == "2":

            users = 0

            c = 1

    while drivers:

        cls()

        print("[ c:\drivers\        ]")
        print("+--------------------+")
        print("|                    |")
        print("| general.drv        |")
        print("| cpu.drv            |")
        print("| ram.drv            |")
        print("| keyB.drv           |")
        print("|                    |")
        print("| [1] Go back        |")
        print("|                    |")
        print("+--------------------+\n")

    while pydos:

        cls()

        print("[ c:\pydos\        ]")
        print("+--------------------+")
        print("|                    |")
        print("| general.drv        |")
        print("| cpu.drv            |")
        print("| ram.drv            |")
        print("| keyB.drv           |")
        print("|                    |")
        print("| [1] Go back        |")
        print("|                    |")
        print("+--------------------+\n")

#commit