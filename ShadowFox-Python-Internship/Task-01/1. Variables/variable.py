#1. Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable. 
    pi=22/7
    print("Value of pi:",pi)
    print("Data type of pi:",type(pi))
#Output:
'''
    Value of pi: 3.14285
    Data type of pi: <class 'float'>
'''

#2. Create a variable called for and assign it a value 4. See what happens and find out the reason behind the behavior that you see.
'''
    for=4
    print(for)
#Output:
    for=4
      ^
    SyntaxError: invalid syntax
'''
#The above code gives an immediate syntax error, python will not allow the code to execute and an error mesage is generated.
#This is because 'for' is a keyword in python. Keywords cannot be used as variable names as it might confuse the interpreter as a loop syntax.
# Fixed version:
    for_value=4
    print("Value of 'for_value':",for_value)
#Output:
'''
    Value of 'for_value': 4
'''

#3. Store the principal amount, rate of interest, and time in different variables and then calculate the Simple Interest for 3 years. Formula: Simple Interest = P x R x T / 100
    principal=10000  #is the Principle amount in currency units
    rate=9           #is the Rate of interest in percentage
    time=3           #is the time in years
    simple_interest=(principal*rate*time)/100  #is the simmple interest
    print("Simple Interest for 3 years is:", simple_interest)
#Output:
'''
    Simple Interest for 3 years is: 2700.0
'''


'''Task-01 1.Variables is completed successfully'''
