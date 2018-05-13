import random
count = 0
reply = ""
lowerLim = 1
upperLim = 100
while reply != "Correct":
    guess = random.randint(lowerLim, upperLim)
    print("Guess is:", guess)
    reply = input("Too high, Too low or Correct: ")
    if reply == "Too high":
        upperLim = guess - 1
    elif reply == "Too low":
        lowerLim = guess + 1
    if (upperLim - lowerLim) < 1:
        print("Invalid game")
    count += 1
print("Got it in %d tries!" %count)
