file = input("Filename(xx.txt): ")
f = open(file, 'r')
lineList = f.read().split("\n")
numLine = len(lineList)
lineNo = -1 #dummy value
while lineNo != 0:
    lineNo = int(input("Line no or 0 to stop: "))
    if lineNo > 0 and lineNo <= numLine:
        print(lineList[lineNo-1])
    elif lineNo > numLine or lineNo < 0:
        print("Invalid line number.")
