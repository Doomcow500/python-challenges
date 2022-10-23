rainy = input("Is it raining?").lower()

if rainy == "yes":
    windy = input("Is it windy?").lower()
    if windy == "yes":
        print("it is too windy for an umbrella!")
    else:
        print("Take an umbrella!")
else:
    print("Enjoy your day!")