# using functions in python

# define a  function that adds numbers
def add_num(num1, num2, num3):
    result = num1 + num2 + num3
    print(f"your result is {result}!")




def main():
    # main logic here
    print("and this...This is a main function")
    
    # call new function
    add_num(5,8,3)
    
# call the main function
if __name__ == "__main__":
    main()
