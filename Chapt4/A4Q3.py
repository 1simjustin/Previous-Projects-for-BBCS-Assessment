file = input("File name(xx.txt): ")
f = open(file, 'r')
wordList = f.read().split('\n')
wordList.sort()
for word in wordList:
    print(word)
listOfWords = {}
mostTimes = 0
for word in wordList:
    if word in listOfWords:
        listOfWords[word] = listOfWords.get(word) + 1
    else:
        listOfWords[word] = 1
for key in listOfWords:
    times = listOfWords.get(key)
    if times > mostTimes:
        mostTimes = times
    print("%s: %d times" %(key, times))
for key in listOfWords:
    if listOfWords.get(key) == mostTimes:
        print(key)
print("was/were found %d times." %mostTimes)
