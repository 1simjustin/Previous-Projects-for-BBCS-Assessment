sumSq = 0
sumCube = 0
largeCube = 0
header1 = "NUMBER"
header2 = "SQUARE"
header3 = "CUBE"
print("%6s%12s%12s" %(header1, header2, header3))
for no in range (1, 15+1):
    sq = pow(no,2)
    cube = pow(no,3)
    sumSq += sq
    sumCube += cube
    if cube > 500:
        largeCube += 1
    print("%6d%12d%12d" %(no, sq, cube))
print("\nSum of Square:", sumSq)
print("Sum of Cubes:", sumCube)
print("No. of cubes above 500:", largeCube)
if sumSq > 2000:
    print("Sum of Squares exceed 2000")
else:
    print("Sum of Squares does not exceed 2000")
