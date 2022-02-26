from Load_Data import csvOpenAndExtra, currentuser
from Edit_Data import Heading_editdata
from Inspect_Data import Heading_checkTimes

def splashscreen():
    print("-----------------------------")
    print("/////////////////////////////")
    print("  anteacheckIN: Automated!")
    print("/////////////////////////////")
    print("-----------------------------")
    input("Press Enter")
    csvOpenAndExtra()
    menu()

def menu():
    while True:
        print("------------------")
        print("-------MENU-------")
        print("------------------")
        print("LOGGED IN AS:", str.upper(currentuser['ï»¿Name']))
        print("------------------")
        print("1. Start Program")
        print("2. Check Sign In/Out times")
        print("3. Edit Sign In/Out times")
        print("4. Change User")

        menuChoice=input("Enter a number from the menu:")

        if menuChoice == "2":
            Heading_checkTimes()
        elif menuChoice == "3":
            Heading_editdata()
        elif menuChoice == "4":
            csvOpenAndExtra()
        else:
            print("Invalid Selection")

splashscreen()