import random

NMIN = 1
NMAX = 100
nChosen = random.randint(NMIN, NMAX)
nGuess = 0
tmp = None
tries = 0

#print(nChosen)

print("I've chosen an integer between", NMIN, "and", NMAX, "- guess it!")

while nGuess != nChosen:
    tries += 1
    try:
        tmp = int(input(""))
    except ValueError:
        print("That wasn't an integer!")
        continue
    nGuess = tmp
    if nGuess > nChosen:
        print("Too big.")
    elif nGuess < nChosen:
        print("Too small.")
    else:
        print("Correct!")

print("That was", nChosen, end="")
print(". You needed", tries, "attempts.")

input("Press any key to continue ...")
