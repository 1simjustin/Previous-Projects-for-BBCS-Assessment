file1 = input("First file(xx.txt): ")
file2 = input("Second file(xx.txt): ")
f1 = open(file1, "r")
f2 = open(file2, "r")
content1 = f1.read().split("\n")
content2 = f2.read().split("\n")
index1 = len(content1)
index2 = len(content2)
index = max(index1,index2)
count = 0
while content1[count] == content2[count] and count<index-1:
    count += 1
if index1 != index 2:
    print("File 1 has %d lines while file 2 has %d lines." %(index1, index2))
else:
    if content1[count] == content2[count]:
        print("Yes")
    else:
        print("No. Difference spotted at line", (count+1))
        print("First file:", content1[count])
        print("Second file:", content2[count])
