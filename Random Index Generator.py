'''
RNG Generator
'''
import random
import time
noStud = int(input("Number of students in class: "))
grpMax = int(input("Number of students per group: "))
CTgroup = [0]*noStud
index = -1
studCount = 0
grpCount = 0
while studCount < noStud:
    grpMem = 0
    if (noStud - grpCount*grpMax) >= grpMax:
        grpSize = grpMax
    else:
        grpSize = noStud - (grpCount)*grpMax
    while grpSize > grpMem:
        index = random.randint(1,noStud)
        if index not in CTgroup:
            CTgroup[studCount] = index
            studCount += 1
            grpMem += 1
            print(index, end='\t')
            #time.sleep(0.1)
    grpCount += 1
    print()
while True:
    print(end="")
