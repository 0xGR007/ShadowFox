'''
1. Write a program to determine the BMI Category based on user input.
Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"
Example:
Enter height in meters: 1.75
Enter weight in kilograms: 70
Output: "Normal"
'''
# Get user input
height=float(input("Enter your height in meters: "))
weight=float(input("Enter your weight in kilograms: "))
# Calculate BMI
bmi=weight / (height ** 2)
# Determine category
if bmi>=30:
    category="Obesity"
elif bmi>=25:
    category="Overweight"
elif bmi>=18.5:
    category="Normal"
else:
    category="Underweight"
print(f"Your BMI is {bmi:.2f}. Category: {category}") # Output result
#Output:
'''
	Enter your height in meters: 1.75
	Enter your weight in kilograms: 70
	Your BMI is 22.86.
	Category: Normal
'''
print("-"*32)


'''Task-01 4. If Condition-1 is completed successfully'''
