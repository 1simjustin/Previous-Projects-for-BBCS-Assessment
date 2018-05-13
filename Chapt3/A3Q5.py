filename = input("Name of file(xx.txt): ")
f = open(filename, "r")
indivDetail = f.read().split("\n")
noWorkers = len(indivDetail)
print("Last name\tHourly Wage\tHours Worked")
print("-"*8*3)
for worker in range (noWorkers):
    name, wage, hour = indivDetail[worker].split()
    print("name\twage\thour")
