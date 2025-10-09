'''
3. Write a program to check if two cities belong to the same country.
Ask the user to enter two cities and print whether they belong to the
same country or not.
Example:
Enter the first city: "Mumbai"
Enter the second city: "Chennai"
Output: "Both cities are in India"
Example:
Enter the first city: "Sydney"
Enter the second city: "Dubai"
Output: "They don't belong to the same country"
'''
# Define the cities in each country
Australia=["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE=["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India=["Mumbai", "Bangalore", "Chennai", "Delhi"]
# Ask user for input
city1=input("Enter the first city: ").strip()
city2=input("Enter the second city: ").strip()
# Function to find which country a city belongs to
def find_country(city):
    if city in Australia:
        return "Australia"
    elif city in UAE:
        return "UAE"
    elif city in India:
        return "India"
    else:
        return None
# Get the countries of both cities
country1=find_country(city1)
country2=find_country(city2)
# Check and print result
if country1 and country2:
    if country1==country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the list")
#Output:
'''
	Enter the first city: Sydney
	Enter the second city: Dubai
	They don't belong to the same country
'''
print("-"*32)


'''Task-01 4. If Condition-3 is completed successfully'''
