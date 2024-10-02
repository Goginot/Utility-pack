
from os import system 

__version__ = "BETA 1.0"

def main_menu():
    global bind_key,active
    while True:
        system("cls")
        print(f"/< Utility pack {__version__} BETA />")
        print("____________________________")   
        print("     1) Record Macros") 
        print("     2) Play macros") 
        print("      3) Info|")
        print("      4) Exit|")
        print("___________________________")
        a = input("Main menu >>> ")
        if a == "1" or a == "1)":
            pass
        elif a == "2" or a == "2)":
            pass        
        elif a == "4" or a == "4)":
            exit()
        elif a == "3" or a == "3)": 
            system("cls")
            print("---------------------------")
            print("     --  Creators  -- ")
            print(" Goginot / Github.goginot")
            print("---------------------------")
            print("      --    Info   -- ")
            print("Version:",__version__)
            print("OS : Windows ")
            print("Lang - Python")
            print("---------------------------")
            print("Thank you for using this program!")
            print("You can also join the development")
            print("of the program on GitHub!")
            print("---------------------------")
            print("Read all in README.txt and Guide.txt! ")
            input("BACK >>> ")










main_menu()