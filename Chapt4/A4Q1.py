file = input("File name(xx.txt): ")
f = open(file, "r")
numList = f.read().split()
numList.sort()
noNum = len(numList)
if noNum%2 == 0:
    highMedIndex = noNum / 2
    lowMedIndex = highMedIndex + 1
    med = (numList[highMedIndex] + numList[lowMedIndex]) / 2
else:
    index = int(noNum/2)+1
    med = numList[index]
numDict = {}
for num in numList:
    num = int(num)
    if num in numDict:
        numDict[num] = numDict.get(num) + 1
    else:
        numDict[num] = 1
mod = 0
for num in numDict:
    numRecur = numDict.get(num)
    if numRecur > mod:
        mod = num
print("Median:", med)
print("Mode:", mod)
