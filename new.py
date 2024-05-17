import os

def cls():

    os.system('clear')

#Clears the screen, only works on linux rn tho

runtime = 1

#Main variable that runs to make sure you can go between menus

start = 1

#The main menu

lock = 0

#The lock screen

password = ""

#Sets the password

setp = 0

#The menu where you type a new password

setnp = 0

#The actual interface for where you will type your new password

confnp = 0

#The screen that asks you if the password is sufficient

passfail = 0

#Displayed when you incorrectly type your password on the lock screen

disp = 0

#Shows your password

settings = 0

#The settings menu

askforreset = 0

#Prompts you to reset your password

resetfail = 0

#If you mistype your password

passreset = 0

#The screen that tells you that your password has been reset

resetpass = 0

#The part that asks you for your password to reset it initially

setuname = 0

#First step in setting a name

name = "root"

#Declares the user's name

setnewuname = 0

#Asks you for a new name

confnewuname = 0

#Confirms your new name

dispuname = 0

#Displays your new name

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

            #Closes the main menu

            settings = 1

            #Opens settings

            #All commands set the current variable to zero in oreder to close the current menu, then sets the variabe associated with the menu they want to go to to one> :3
        
        if a == "q":

            cls()

            quit()

            #Closes the file on your machine

        if a == "l":

            if password != "":

                #!= is not equal, I think...

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

                #I should use !=

                start = 0

                disp = 1

            else:

                start = 0
                
                passfail = 1


    while lock:

    #Lock screen
    
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

        if a == "q":

            cls()

            quit()

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
        print("f - fully reset PyShell") #Sets the username to root, the password and hostname to nothing
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