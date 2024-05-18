import os

def cls():

    os.system('cls' if os.name == 'nt' else 'clear')

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

sethname = 0

#Asks you if you want to set a new host name

host = ""

#Host name is not set at the start

disph = 0

#Displays the host name

disphfail = 0

#Screen that is shown if no host name is set

asknewhname = 0

#Asks you for a new host name

confhname = 0

#Confirms the new host name

pyInfo = 0

#The screen that shows the PyShell info

resetconf = 0

#Asks you if you are sure about resetting PyShell

confresetpass = 0

#Asks for your password to reset PyShell

resetdone = 0

#The screen that tells you that you've successfully reset PyShell, you monster >:(

boot = 0

#The variable that runs the loaded OS outside of the shell

bootconf = 0

#Confirms if you want to boot into the OS

fullboot = 0

#The actual OS boot variable :3

bootsetup = 0

#Makes sure you have a username and password to boot the OS

pwd = "/"

root = ["/user-files" , "/about" , "/extra-stuff"]

userfiles = ["example.txt"]

about = ["version.txt" , "credits.txt" , "license.txt"]

extrastuff = ["commands.txt" , "inspirations.txt"]

ls = root

PyLinuxLock = 0

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

        if a == "b":

            start = 0

            bootconf = 1
        
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
        print("Type anything to go back\n")

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

        if a == "f":
        
            settings = 0

            resetconf = 1
        
        if a == "a":

            settings = 0

            pyInfo = 1

        if a == "h":

            settings = 0

            sethname = 1

        if a == "p":

            if not host == "":

                settings = 0

                disph = 1

            else:

                settings = 0

                disphfail = 1

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

        print("You are currently set as '" + name + "'.")
        print("Type anything to go back\n")

        a = input("> ")

        dispuname = 0

        settings = 1

    while sethname:

        cls()

        print("PyShell lite\n")

        print("n - set a new host name")
        print("b - go back\n")

        a = input("> ")

        if a == "n":

            sethname = 0

            asknewhname = 1

        if a == "b":

            sethname = 0

            settings = 1

    while asknewhname:

        cls()

        print("PyShell lite\n")

        print("Type your new host name\n")

        host = input("> ")

        asknewhname = 0

        confhname = 1

    while confhname:

        cls()

        print("PyShell lite\n")

        print("Is '" + host + "' okay?\n")

        print("y - yes")
        print("n - no\n")

        a = input("> ")

        if a == "y":

            confhname = 0

            settings = 1

        if a == "n":

            confhname = 0    

            asknewhname = 1

    while disph:

        cls()

        print("PyShell lite\n")

        print("Your host name is '" + host + "'.")
        print("Type anything to go back\n")

        a = input("> ")

        disph = 0

        settings = 1

    while disphfail:

        cls()

        print("PyShell lite\n")

        print("No host name has been set.")
        print("Type anything to go back\n")

        a = input("> ")

        disphfail = 0

        settings = 1

    while pyInfo:

        cls()

        print("PyShell lite\n")

        print("PyShell v1.0.0")
        print("By Franco M.\n")

        print("Based off of Bash, the GNU project, Linux, and Unix\n")

        print("Made by Franco M. in Visual Studio Code by Microsoft with Python by Guido van Rossum")
        print("Type anything to go back\n")

        a = input("> ")

        pyInfo = 0

        settings = 1

    while resetconf:

        cls()

        print("PyShell lite\n")

        print("Are you sure you want to fully reset PyShell?\n")

        print("y - yes")
        print("n - no\n")

        a = input("> ")

        if a == "n":

            resetconf = 0

            settings = 1

        if a == "y":

            resetconf = 0
            
            confresetpass = 1

    while confresetpass:

        if not password == "":

            cls()

            print("PyShell lite\n")

            print("Please type your password\n")

            a = input("> ")

            if a == password:

                name = "root"

                password = ""

                host = ""

                confresetpass = 0

                resetdone = 1

            else:

                confresetpass = 0

                resetconf = 1

        else:

            confresetpass = 0

            resetdone = 1

    while resetdone:

        cls()

        print("PyShell lite\n")

        print("PyShell has successfully been reset.")
        print("Type anything to go back\n")

        a = input("> ")

        resetdone = 0

        settings = 1

    while bootconf:

        cls()

        print("PyShell lite\n")

        print("Are you sure you want to boot into the OS?\n")

        print("y - yes")
        print("n - no\n")

        a  = input("> ")

        if a == "y":

            start = 0

            bootconf = 0

            if host == "":    
                
                host = "PyLinux"

            else:

                host = host

            fullboot = 1

            runtime = 0

            cls()

            print("Type 'help' for a list of commands")

        if a == "n":

            bootconf = 0

            start = 1


while fullboot:

    a = input(name + "@" + host + pwd + "$ ")

    if a == "pwd":

        print(pwd)

    if a == "ls":

        print('   '.join(ls))

    if a == "help":

        print("help - prints this help message")
        print("pwd - prints the current directory")
        print("ls - list the current directory")
        print("cd - changes the directory to a specified directory")
        print("   ex - cd /about")
        print("cat - reads a specified file")
        print("   ex - cat example.txt")
        print("whoami - prints your name, password, and user permissions")
        print("lock - locks the OS, only works if you have a password set")
        print("chname - changes your user name")
        print("chpass - changes your password")
        print("chhost - changes the host name")
        print("clear - clears the screen")
        print("exit - shuts off PyLinux")
        print("")

    if a == "whoami":

        print("Name: " + name)
        
        if not password == "":
            
            print("Password: " + password)

        else:

            print("Password: No password set")

        print("User permissions: Absolute")

    if a == "lock":

        if not password == "":

            fullboot = 0

            PyLinuxLock = 1

        else:

            print("You have no password set.")

    while PyLinuxLock:

        cls()

        print("PyLinux v1.0.0\n")

        print("[1] Enter password")
        print("[2] Exit PyLinux\n")

        a = input("> ")

        if a == "1":

            cls()

            print("PyLinux v1.0.0\n")

            print("Please enter your password\n")

            a = input("> ")

            if a == password:

                cls()
                
                print("Type 'help' for a list of commands")

                fullboot = 1
            
                PyLinuxLock = 0

            else:

                cls()

                PyLinuxLock = 1