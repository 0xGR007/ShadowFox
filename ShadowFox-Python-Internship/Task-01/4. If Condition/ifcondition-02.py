'''
2. Write a program to determine which country a city belongs to. Given list of cities per country:
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
Ask the user to enter a city name and print the corresponding country.
Example:
Enter a city name: "Abu Dhabi"
Output: "Abu Dhabi is in UAE"
'''
#City Database 
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
city = input("Enter a city name: ").strip() # Get user input
# Determine city
if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print(f"Sorry, {city} is not in our City database.") #if city not in database
#Output:
'''
	Enter a city name: Abu Dhabi
	Abu Dhabi is in UAE
'''
print("-"*32)


'''Task-01 4. If Condition-2 is completed successfully'''
