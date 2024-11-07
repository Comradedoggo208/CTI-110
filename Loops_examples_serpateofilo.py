# for loop using range function with one perameter
# parameter is the stop value, stop value is not inclusive
'''
for var in range(5):
    print(var+1)
    #print("apples are delicious!")
'''

# for loop using the range function with two parameters
# parameters are the start value and the stop value, the stop is not inclusive
'''
end_num = 14

for item in range(7,end_num+1):
    print(item)
'''    

# for loop with 3 parameters
# parameters are teh Start, Stop (non-inclusive), and the increment/number to increase by
'''
for cat in range(0,101,5):
    print(cat)
'''
#loop through a list and print each item
'''
mylist = ["uno", 2, 2.5, "threse", 4, 4.5, "sinco", False]

for numb in mylist:
    print(numb)
'''
numblist = [10, 20, 30, 40, 50]

total = 0
for num in numblist:
    total = total + num
print(f"your final total is {total}")
