import random
gameNo = 0
guessPerGame = 6
guessDict = {}
for guessNo in range (1, guessPerGame+1):
    guessDict[guessNo] = 0
unsuc = 0
sucGames = 0
sucGameTries = 0
while gameNo < 10:
    number = random.randint(1,50)
    print(number)
    gameNo += 1
    guessNo = 0
    guess = 0
    print("Game No:", gameNo)
    while guessNo < guessPerGame and guess != number:
        guess = input("Guess a number [1-50]: ")
        if guess.isdigit() == False:
            print("Invalid input, try again.")
        else:
            guessNo += 1
            guess = int(guess)
            if guess < number:
                print("Too low")
            if guess > number:
                print("Too high")
            if guess == number:
                print("Congratulations!")
    if guessNo == guessPerGame:
        print("Sorry, you did not get it right. The answer is", number)
        unsuc += 1
    else:
        guessDict[guessNo] = guessDict.get(guessNo) + 1
        sucGames += 1
        sucGameTries += guessNo
    print()
print()
header = "NumGuess\tNumGames"
print(header)
for guessCount in range (1, guessPerGame+1):
    numGuess = guessCount
    numGames = guessDict.get(guessCount)
    print("%d\t\t%d" %(numGuess, numGames))
print("Unsuccessful games:", unsuc)
if sucGames == 0:
    print("No successful games to calculate avg")
else:
    avgSucGameTries = sucGameTries / sucGames
    print("Avg num of tries for successful games: %.2f" %avgSucGameTries)
