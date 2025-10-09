#1. Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string. Print the result. Try to identify the representation used.
def format_number(n,s):
  return format(n,s)
formatted_string=format_number(145, 'o')
print("Formatted string:",formatted_string) # 'o' represents octal format
#Output:
'''
    Formatted string: 221
'''
print("-"*32)

#2. In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula: Circle Area = π r^2. (Use the value 3.14 for π)
#Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount of water in the pond? Print the answer without any decimal point in it.
#Hint: Circle Area = π r^2. Water in the pond = Pond Area Water per Square Meter.
def pond_area(radius):
    pi=3.14
    return pi*(radius**2)
radius=84
pond_area=pond_area(radius)
print("Area of the pond:",pond_area)
#Output:
'''
    Area of the pond: 22155.84
'''
#Bonus Question:
water=1.4
total_water=water*pond_area
print("Total amount of water in the pond:",int(total_water)) # Removing decimal points
#Output:
'''
    Total amount of water in the pond: 31018.176
'''
print("-"*32)

#3. If you cross a 490meterlong street in 7 minutes, calculate your speed in meters per second. Print the answer without any decimal point in it. Hint: Speed = Distance / Time
def speed(distance, time_minutes):
    time_seconds=time_minutes * 60  # Convert time to seconds because speed in meters per second
    speed=distance / time_seconds
    return int(speed)  # Removing decimal points
distance=490
time_minutes=7
speed=speed(distance,time_minutes)
print("Speed in meters per second:",speed)
#Output:
'''
    Speed in meters per second: 1
'''
print("-"*32)


'''Task-01 2.Numbers is completed successfully'''
