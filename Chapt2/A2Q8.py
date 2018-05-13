import random
maxPot = 0
noRolls = 0
pot = int(input("How much initial pot: "))
while pot != 0:
    no1 = random.randint(1,6)
    no2 = random.randint(1,6)
    if no1+no2 != 7:
        pot -= 1
    else:
        pot += 4
    noRolls += 1
    if pot > maxPot:
        maxPot = pot
print("%d rolls taken to break player. Max pot is $%d" %(noRolls, maxPot))
