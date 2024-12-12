'''
Teofilo A Serpa
P4HW1
11/12/24
'''

#ask the usr how many scores they want to enter
grades = int(input("How many scores would you like the enter?: "))
print()

# have a list to put grades into
gradeList = []

# loop it! 
for pointavg in range(grades):
    grade = int(input(f"Enter Score #{pointavg+1}: "))

    while grade < 0 or grade > 100:
        print(f"{grade} is the wrong Score. it must be between 0-100")
        grade = int(input(f"Enter Score #{pointavg+1} again: "))

    gradeList.append(grade)

#loops to print grades
print()
print("your grades are: ")
for score in gradeList:
    print(score)

print("---------------Results---------------")
print(f"the Lowest Grade: {min(gradeList)}")
print(f"The Highest Grade: {max(gradeList)}")
print(f"The Sum of the Grades are {sum(gradeList)}")
avg = sum(gradeList)/len(gradeList)
print(f"the Average of the grades is: {avg:.2f}")
print("--"*25)

avg = sum(gradeList)/len(gradeList)



if avg >= 90:
    Grade = "A"

elif avg >= 80:
    Grade = "B"

elif avg >= 70:
    Grade = "C"

elif avg >= 60:
    Grade = "D"

elif avg <= 59:
    Grade = "F"

print(f"Your Grade is a/an: {Grade}")
