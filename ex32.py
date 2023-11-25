print('''You enter a dark room with two doors.
Do you go through door #1 or door #2?''')

door = input("> ")

if door == "1":
    print("There is a giant bear eating a cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off then calmly finishes his cake. Fool!")
    elif bear == "2":
        print("The bear bashes your head, eats his cake, then eats your legs.")
    else:
        print(f"Good thinking. {bear} is probably a better move.")
        print("The bear decides you must be mad and runs away.")

elif door == "2":
    print("You stare into the endless abyss of Cthulhu's left eyeball.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives, but is powered by a bowl of jelly.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck, and your liquefied brain drips slowly out.")
        print("Good job!")

else:
    print("You stumble around and trip straight onto a metal bar and die screaming. Good job!")
