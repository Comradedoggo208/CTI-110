'''
Teofilo A. Serpa
10/24/24
P3HW1
create a program to calculate the highest, lowest, sum, and average of test grades
'''
mod1 = float(input("Input Grade for Mod 1 test: "))
print()
mod2 = float(input("Input Grade for Mod 2 test: "))
print()
mod3 = float(input("Input Grade for Mod 3 test: "))
print()
mod4 = float(input("Input Grade for Mod 4 test: "))
print()
mod5 = float(input("Input Grade for Mod 5 test: "))
print()
mod6 = float(input("Input Grade for Mod 6 test: "))
print()
Test_grades = [mod1, mod2, mod3, mod4, mod5, mod6]
print("---------------Results---------------")
print(f"the Lowest Grade: {min(Test_grades)}")
print(f"The Highest Grade: {max(Test_grades)}")
print(f"The Sum of the Grades are {sum(Test_grades)}")
avg = sum(Test_grades)/len(Test_grades)
print(f"the Average of the grades is: {avg:.2f}")
print("--"*25)

avg = sum(Test_grades)/len(Test_grades)



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
