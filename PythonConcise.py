from math import pi


def radius():
    try:
        r = int(input ("Enter the radius: "))
        area = pi * r ** 2
        print(f"The area of a circle with radius {r} is {area}")
        
        def restart():
            restart = input("Would you like to calculate another radius?: \n(YES/Y) or (NO/N) :")
            if restart.upper() == "YES" or restart.upper() == "Y":
                radius()
            if restart.upper() == "NO" or restart.upper() == "YES":
                print("Script terminating. Goodbye.")
            if restart.upper() != "Y" or restart.upper() != "N":
                restart()
        restart()
    except ValueError:
        print("Please enter radius in numbers only !")
        radius()
    except TypeError:
        print("Invalid Input !")
        restart()
radius()

