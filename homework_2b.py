# Clark, Julien
# Computer Programming, period < 4>
# Assignment 2b
# 10/16/26

#Version 1: Green alien
alien_color = 'green'
if alien_color == 'green':
    print("The player just earned 5 points.")
else:
    print("The player just earned 10 points.")


alien_color = 'yellow'
if alien_color == 'green':
    print("The player just earned 5 points.")
else:
    print("The player just earned 10 points.")
print()


for color in ['green', 'yellow', 'red']:
    alien_color = color
    if alien_color == 'green':
        print(f"Alien is {alien_color}: You earned 5 points.")
    elif alien_color == 'yellow':
        print(f"Alien is {alien_color}: You earned 10 points.")
    else:
        print(f"Alien is {alien_color}: You earned 15 points.")
print()

test_ages = [1, 3.9, 10, 13, 19, 20, 21, 65]

for age in test_ages:
    if age < 2:
        print(f"Age {age}: Baby")
    elif age < 4:
        print(f"Age {age}: Toddler")
    elif age < 13:
        print(f"Age {age}: Kid")
    elif age < 20:
        print(f"Age {age}: Teenager")
    elif age < 65:
        print(f"Age {age}: Adult")
    else:
        print(f"Age {age}: Elder")
print()

# Test 1: Populated list
usernames = ['admin', 'jaden', 'sarah', 'eric', 'charlie']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")


usernames = []
print("\n[Testing empty list]")
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
print()






current_users = ['john', 'sarah', 'admin', 'eric', 'jessica']
current_users_lower = [user.lower() for user in current_users]

new_users = ['JOHN', 'michel', 'DAVID', 'Sarah', 'alex']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"Username '{new_user}' is available.")
print()



#Ordinal Numbers


numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")