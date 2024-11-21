# using functions in python

# define a  function that adds numbers
def add_num(num1, num2, num3):
    result = num1 + num2 + num3
    return result




def main():
    # main logic here
    print("and this...This is a main function")
    
    # call new function
   result1 = add_num(5,8,3)
    print(result1)
    print("adding the result1 variable to some 0's")
    print(add_num(result1,1,1))
    
# call the main function
if __name__ == "__main__":
    main()
