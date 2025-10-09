'''
1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20 times).
Count and print the following statistics:
How many times you rolled a 6
How many times you rolled a 1
How many times you rolled two 6s in a row
'''
import random
six_count=0
one_count=0
two_six_count=0
last_roll=0
for i in range(20):  # roll the die 20 times
    roll=random.randint(1, 6)
    print(f"Roll {i+1} : {roll}")
    if roll==6:
        six_count+=1
    if roll==1:
        one_count+=1
    if roll==6 and last_roll==6:
        two_six_count+=1
    last_roll=roll
print(six_count,"times you rolled 6")
print(one_count,"times you rolled 1")
print(two_six_count,"times you rolled two 6s in a row")
#Output:
'''
	Roll 1 : 3
	Roll 2 : 2
	Roll 3 : 3
	Roll 4 : 2
	Roll 5 : 6
	Roll 6 : 6
	Roll 7 : 4
	Roll 8 : 4
	Roll 9 : 6
	Roll 10 : 6
	Roll 11 : 5
	Roll 12 : 5
	Roll 13 : 5
	Roll 14 : 1
	Roll 15 : 2
	Roll 16 : 5
	Roll 17 : 3
	Roll 18 : 6
	Roll 19 : 3
	Roll 20 : 4
	5 times you rolled 6
	1 times you rolled 1
	2 times you rolled two 6s in a row
'''
print("-"*32)


'''Task-01 5. For Loop-01 is completed successfully'''
