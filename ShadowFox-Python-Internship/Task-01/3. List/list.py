#You have a list of superheroes representing the Justice League.
justice_league=["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"] 
print("Initial list:",justice_league)
#Output:
'''
	Initial list: ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern']
'''
print("-"*32)

#Perform the following tasks: 
#1. Calculate the number of members in the Justice League.
print("Number of members:",len(justice_league))
#Output:
'''
	Number of members: 6
'''
print("-"*32)

#2. Batman recruited Batgirl and Nightwing as new members. Add them to your list. 
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:",justice_league)
#Output:
'''
	After adding Batgirl and Nightwing: ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
'''
print("-"*32)

#3. Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.
justice_league.remove("Wonder Woman")
justice_league.insert(0,"Wonder Woman")
print("After moving Wonder Woman to the beginning:",justice_league)
#Output:
'''
	After moving Wonder Woman to the beginning: ['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
'''
print("-"*32)

#4. Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash. 
justice_league.remove("Green Lantern")
flash_index=justice_league.index("Flash")
justice_league.insert(flash_index,"Green Lantern")  # or "Superman"
print("Separated Aquaman & Flash:",justice_league)
#Output:
'''
	Separated Aquaman & Flash: ['Wonder Woman', 'Superman', 'Batman', 'Green Lantern', 'Flash', 'Aquaman', 'Batgirl', 'Nightwing']
'''
print("-"*32)

#5. The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the following new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow". 
new_justice_league=["Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow"]
justice_league=new_justice_league
print("New Team:", justice_league)
#Output:
'''
	New Team: ['Cyborg', 'Shazam', 'Hawkgirl', 'Martian Manhunter', 'Green Arrow']
'''
print("-"*32)

#6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
justice_league.sort()
print("Sorted team:",justice_league)
print("New leader (index 0):",justice_league[0])
#Output:
'''
	Sorted team: ['Cyborg', 'Green Arrow', 'Hawkgirl', 'Martian Manhunter', 'Shazam']
	New leader (index 0): Cyborg
'''
print("-"*32)


'''Task-01 3.List is completed successfully'''
