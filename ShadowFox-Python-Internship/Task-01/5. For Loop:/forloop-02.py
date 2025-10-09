'''
2. Imagine you are doing a workout routine, and you have to complete 100 jumping jacks.
Write a program that:
Asks you to perform 10 jumping jacks at a time.
After each set, it asks, "Are you tired?"
If you reply "yes" or "y," it should ask if you want to skip the remaining sets.
If you reply "yes" or "y," it should break and print, "You completed a total of jumping jacks."
For example, if you did only 30 jumping jacks and answered "yes," the program
will break and print, "You completed a total of 30 jumping jacks."
If you reply "no" or "n," it should continue and display how many jumping jacks
are remaining. After that, ask you again, "Are you tired?"
For example, if you answered "no," it should display that 70 jumping jacks are
remaining and ask you again, "Are you tired?"
If you reply "no" or "n," it should continue and display how many jumping jacks
are remaining. After that, ask you again, "Are you tired?"
For example, if you answered "no," it should display that 70 jumping jacks are
remaining and ask you again, "Are you tired?"
If you complete all 100 jumping jacks, it should print, "Congratulations! You
completed the workout," and stop the program
'''
total=100
step=10
for done in range(step,total+1,step):
    print(f"You completed {done} jumping jacks.")
    if done==total:
        print("Congratulations! You completed the workout.")
        break
    tired=input("Are you tired? (yes/y or no/n):").lower()
    if tired in ["yes","y"]:
        skip=input("Do you want to skip the rest? (yes/y or no/n):").lower()
        if skip in ["yes","y"]:
            print(f"You completed a total of {done} jumping jacks.")
            break
        else:
            left=total-done
            print(f"{left} jumping jacks remaining.")
    else:
        left=total-done
        print(f"{left} jumping jacks remaining.")
#Output:
'''
	You completed 10 jumping jacks.
	Are you tired? (yes/y or no/n):n
	90 jumping jacks remaining.
	You completed 20 jumping jacks.
	Are you tired? (yes/y or no/n):n
	80 jumping jacks remaining.
	You completed 30 jumping jacks.
	Are you tired? (yes/y or no/n):n
	70 jumping jacks remaining.
	You completed 40 jumping jacks.
	Are you tired? (yes/y or no/n):n
	60 jumping jacks remaining.
	You completed 50 jumping jacks.
	Are you tired? (yes/y or no/n):n
	50 jumping jacks remaining.
	You completed 60 jumping jacks.
	Are you tired? (yes/y or no/n):y
	Do you want to skip the rest? (yes/y or no/n):n
	40 jumping jacks remaining.
	You completed 70 jumping jacks.
	Are you tired? (yes/y or no/n):n
	30 jumping jacks remaining.
	You completed 80 jumping jacks.
	Are you tired? (yes/y or no/n):y
	Do you want to skip the rest? (yes/y or no/n):y
	You completed a total of 80 jumping jacks.
'''
print("-"*32)


'''Task-01 5. For Loop-02 is completed successfully'''
