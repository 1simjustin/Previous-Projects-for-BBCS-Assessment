numbers = input("Enter a series of single-digit numbers: ")
if numbers.isdigit() == False:
    print("Invalid input, try again.")
    numbers = input("Enter a series of single-digit numbers: ")
numList = []
for num in numbers:
    numList.append(int(num))
total = 0
largest = 0
for num in numList:
    total += num
    if num > largest:
        largest = num
noNum = len(numList)
avg = total / noNum
print("Sum of digits:", total)
print("Avg of digits:", avg)
print("Largest digit:", largest)
