A = int(input("First no: "))
B = int(input("Seconf no: "))
largeNo = 0
smallNo = 0
if A > B:
    largeNo = A
    smalNo = B
else:
    largeNo = B
    smallNo = A
while smallNo != 0:
    div = largeNo % smallNo
    largeNo = smallNo
    smallNo = div
print("GCD is", largeNo)
