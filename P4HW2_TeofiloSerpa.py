#Teofilo Serpa
#11/14/24
#P4HW2
#create a program that claculates a paycheck based on overtime pay

#create variables to hold totals
numEmp = 0
totalOTpay = 0.00
totalpay = 0.00
totalGrosspay = 0.00

# make variable to control loop
emp_name = input("Enter Employee name or 'done' to terminate: ")

while emp_name.lower() != "done":
    numEmp += 1
    
    emp_hours = int(input("How many HOURS did you work?: "))

    pay_rate = float(input("What is your regular Pay Rate?: "))

    print("+-"*18)
    print(f"Employee Name: {emp_name}")
    print()
    if emp_hours > 40:
        OT = (emp_hours - 40)
        OT_pay_rate = (pay_rate * 1.5)
        OT_pay = (OT * OT_pay_rate)
        Reg_pay = (pay_rate * 40)
        G_pay = (OT_pay + Reg_pay)

    else:
        OT = (emp_hours - 40)
        OT_pay_rate = (pay_rate * 1.5)
        OT_pay = (OT * OT_pay_rate)
        Reg_pay = (pay_rate * emp_hours)
        G_pay = Reg_pay
    
    totalpay += Reg_pay
    totalOTpay += OT_pay
    totalGrosspay += G_pay

    print(f"{'Hours worked':<10}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<10}{'Reg/Hourly Pay':<10}{'Gross Pay':<10}")
    print("+-"*30)
    print(f"${emp_hours:<10}${pay_rate:<10}{OT:<10}${OT_pay:<10.2f}${Reg_pay:<10.2f}${G_pay:<10.2f}")
    print()
    emp_name = input("Enter Employee name or 'done' to terminate: ")
# Oh no, the loop, its broken
print("YOUR LOOP ENDS HERE FRIEZA")
print(f"Total of Employees entered: {numEmp}")
print(f"Total of OverTime pay: ${totalOTpay:.2f}")
print(f"Total of Regular Pay: ${totalpay:.2f}")
print(f"Total of Gross Pay: ${totalGrosspay:.2f}")
