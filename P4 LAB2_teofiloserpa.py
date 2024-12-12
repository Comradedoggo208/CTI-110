'''
Teofilo A Serpa
P4LAB1
11/7/24
Write a program that asks the user to enter an integer.
'''
run_again = "yes"

while run_again != "no":

    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        #display multiplication for the value and range (1-12)
        for item in range(1,13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values")
        
    run_again = input("would you like to run the program again? ")

#loop breaks here, aka user enters 'no'
print("YOUR PROGRAM ENDS HERE ZAMASU!")
