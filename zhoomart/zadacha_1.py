counter = 0

while counter < 3:
    time = input("Enter time: ").lower()

    if time in ["morning", "utro"]:
        print("Good morning")
    elif time in ["afternoon", "den"]:
        print("Good afternoon")
    elif time in ["evening", "vecher"]:
        print("Good evening")
    else:
        print("Hello")