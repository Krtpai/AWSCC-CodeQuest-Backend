def divide(a, b):
    return a / b

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    quotient = divide(a, b)
    print(f"The quotient is {quotient}")
except Exception as e:
    print(f"Invalid input: {e}")
    
#Removing 'else' makes the program much logical. Since leaving that will still
#be executed when no exception occurs, but the variable for 'quotient' might not be 
#defined if an exception occurs within 'try'. 