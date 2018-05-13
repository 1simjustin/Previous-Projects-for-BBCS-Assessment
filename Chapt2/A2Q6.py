largeNo = 0
valueLargeNo = 0
total = 0
for no in range(100,111):
    print("\n%d: " %no, end="")
    for div in range (1, no+1):
        if no%div == 0:
            print("%7d" %div, end="")
            total += div
    print("\nSum of divisors:", total)
    if total > valueLargeNo:
        valueLargeNo = total
        largeNo = no
    total = 0
print()
print(largeNo, "has the largest sum of divisors.")
