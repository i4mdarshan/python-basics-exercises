# ## Exercise: Python for loop
# 1. After flipping a coin 10 times you got this result,
# ```
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ```
# Using for loop figure out how many times you got heads
print("\nExercise 1\n")
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = [res for res in result if res == "heads"]
print(len(count))


# 2. Print square of all numbers between 1 to 10 except even numbers
print("\nExercise 2\n")
print([num*num for num in range(1,10,2)])

# 3. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.
print("\nExercise 3\n")
month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

index = [index for index,exp in enumerate(expense_list) if exp == e]

if index[0]:
    print(f'You spent {e} in {month_list[index[0]]}')
else:
    print(f'You didn\'t spend {e} in any month')

# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message

print("\nExercise 4\n")

for i in range(5):
    print(f"You ran {i+1} miles") # i starts with zero hence adding 1
    tired = input("Are you tired? ")
    if tired == 'yes':
        break

if i == 4: # 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print("You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")

# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```
print("\nExercise 5\n")
line = ""
for i in range(6):
    line = ""
    for j in range(i):
        line += "*"
    print(line)
