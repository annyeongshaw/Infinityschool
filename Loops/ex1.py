#Make a Program that asks for the 4 bimonthly grades and shows the average.

totalGrade = 0
for i in range (1,5):
    grade = float(input("Enter student grade: "))
    totalGrade += grade
average = totalGrade/4
print (f"The student's average is {average}")