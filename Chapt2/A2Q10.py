students = int(input("No. students: "))
countGood = 0
noPass = 0
for grading in range (students):
    sumMarks = 0
    for mark in range (3):
        grade = float(input("Student "+str(grading+1)+" marks for paper "+str(mark+1)+": "))
        sumMarks += grade
    avgMarks = sumMarks / 3
    if avgMarks >= 60:
        print("Student", grading + 1, "passed.")
        noPass += 1
    else:
        print("Student", grading + 1, "failed.\n")
    if avgMarks >= 80:
        print("Good job!\n")
        countGood += 1
print(noPass, "students passed.")
print(countGood, "students scored above 80!")
per = noPass*100/students
if per > 50:
    print("Most students passed!")
