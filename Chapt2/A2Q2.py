string = input("Enter a word: ")
letterCount = 0
vowelCount = 0
for letter in string:
    letterCount += 1
    if letter in "aeiou":
        vowelCount += 1
percentVowel = vowelCount / letterCount
print("Letters:", letterCount)
print("Vowels:", vowelCount)
print("Percent of vowels:", percentVowel)
