import random
number = random.randint(1,100)
guess = 0
count = 0
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess > number:
        print("Too large")
    elif guess < number:
        print("Too small")
    count += 1
print("You got it in %d tries!" %count)
