import os

def cls():

    os.system('clear')

runtime = 1

start = 1

lock = 0

lockfail = 0

password = ""

setp = 0

setnp = 0

confnp = 0

enterp = 0

passfail = 0

disp = 0

askforp = 0

settings = 0

askforreset = 0

resetfail = 0

passreset = 0

resetpass = 0

setuname = 0

name = "root"

setnewuname = 0

confnewuname = 0

dispuname = 0

while runtime:

    while start:

        cls()

        print("PyShell lite\n")

        print("b - boot")
        print("s - settings")
        print("p - set password")
        print("d - show password")
        print("l - lock")
        print("q - quit\n")

        a = input("> ")

        if a == "s":

            start = 0

            settings = 1
        
        if a == "q":

            cls()

            quit()

        if a == "l":

            if password != "":

                start = 0

                lock = 1

            else:

                start = 0

                passfail = 1

        if a == "p":

            start = 0

            setp = 1

        if a == "d":

            cls()

            if not password == "":

                start = 0

                disp = 1

            else:

                start = 0
                
                passfail = 1


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

    while setp:

        cls()

        print("PyShell lite\n")

        print("n - type a new password")
        print("b - go back\n")

        a = input("> ")

        if a == "b":

            setp = 0

            start = 1

        if a == "n":

            setp = 0

            setnp = 1

    while setnp:

        cls()

        print("PyShell lite\n")

        print("Type a new password\n")

        password = input("> ")

        setnp = 0
        
        confnp = 1

    while confnp:

        cls()

        print("PyShell lite\n")

        print("Is '" + password + "' ok?\n")

        print("y - yes")
        print("n - no\n")

        a = input("> ")

        if a == "y":

            confnp = 0

            start = 1

        if a == "n":

            confnp = 0

            setnp = 1

    while disp:

        cls()

        print("PyShell lite\n")

        print("Your password is '" + password + "'.")
        print("Type anything to go back to the main menu\n")

        a = input("> ")

        disp = 0

        start = 1

    while passfail:

        cls()

        print("PyShell lite\n")

        print("No password has been set, type anything to go back\n")

        a = input("> ")

        passfail = 0

        start = 1

    while settings:

        cls()

        print("PyShell lite\n")

        print("r - reset password")
        print("n - set a user name")
        print("u - show user name")
        print("h - set a host name")
        print("p - show host name")
        print("a - show PyShell info")
        print("f - fully reset PyShell")
        print("b - go back\n")

        a = input("> ")

        if a == "u":

            settings = 0

            dispuname = 1

        if a == "n":

            settings = 0

            setuname = 1

        if a == "r":

            if not password == "":
            
                settings = 0
            
                askforreset = 1

            else:

                settings = 0

                resetfail = 1
        
        if a == "b":

            settings = 0

            start = 1
    
    while askforreset:

        cls()
        
        print("PyShell lite\n")

        print("e - enter your password")
        print("b - go back\n")

        a = input("> ")

        if a == "e":

            askforreset = 0

            resetpass = 1

        if a == "b":

            askforreset = 0
            
            settings = 1

    while resetpass:

        cls()
        
        print("PyShell lite\n")

        print("Please enter your password\n")

        a = input("> ")

        if a == password:

            resetpass = 0

            passreset = 1

            password = ""

        else:

            resetpass = 0

            settings = 1



    while resetfail:

        cls()

        print("PyShell lite\n")

        print("No password has been set, type anything to go back.\n")

        a = input("> ")

        resetfail = 0

        settings = 1

    while passreset:

        cls()
        
        print("PyShell lite\n")

        print("Your password has been reset, type anything to go back.\n")

        a = input("> ")

        askforreset = 0

        passreset = 0

        settings = 1

    while setuname:

        cls()

        print("PyShell lite\n")

        print("n - set a new username")
        print("b - go back\n")

        a = input("> ")

        if a == "n":

            setuname = 0

            setnewuname = 1

        if a == "b":

            setuname = 0

            settings = 1

    while setnewuname:

        cls()

        print("PyShell lite\n")

        print("Type your new name\n")

        name = input("> ")

        setnewuname = 0

        confnewuname = 1

    while confnewuname:

        cls()

        print("PyShell lite\n")

        print("Is '" + name + "' okay?\n")

        print("y - yes")
        print("n - no\n")

        a = input("> ")

        if a == "y":

            confnewuname = 0

            settings = 1

        if a == "n":

            confnewuname = 0

            setnewuname = 1

    while dispuname:

        cls()

        print("PyShell lite\n")

        print("You are currently set as '" + name + "'. Press any key to go back\n")

        a = input("> ")

        dispuname = 0

        settings = 1