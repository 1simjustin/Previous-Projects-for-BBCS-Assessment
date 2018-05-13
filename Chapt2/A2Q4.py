n = int(input("Value of n: "))
star = "*"
blank = " "
if n>0:
    for i in range (n):
        if i ==0 or i == n-1:
            print(star*2*n)
        else:
            print(star+blank*(2*n-2)+star)
else:
    print("Invalid")
