# Exercise 1

# TASKS:
# Starter code:
# age = 19
# driver_license = True
# As a user I should be able to keep being prompted for input until I say 'exit'.
# Different results:
# You can vote and drive.
# You can vote.
# You can drive.
# You can not legally drink, but your mates/uncles might have your back (bigger 16)
# You are too young, go back to school.

age = 19 # Variable to check the age
driver_license = True # Variable to check if they have driving license

# Function to ask the age to the user from input and return this value
def ask_age():
    user_age = input("Please enter your age (ONLY DIGITS): ")
    while user_age.isdigit() == False:
        user_age = input("Try again... (ONLY DIGITS): ")
    return  user_age

# Function to ask to the user if they have driving license and return True if Yes or False if No
def ask_driver_license():
    check_license = input("Do you have driving license? (Y/N): ")
    while check_license != "Y" and check_license != "N":
        check_license = input("Try again... (Y/N): ")
    if check_license == "Y":
        return True
    else:
        return False

# Let's create the program and stop it when the user wants to stop
print("WELCOME!")
print("Let's go to check if you can drive or vote!")
run_program = True
while run_program:
    # Ask the user if they want to stop or continue with the program
    user_input = input("Would you like to continue? (GO/EXIT): ")
    if user_input == "EXIT": # If they want to exit
        run_program = False
    elif user_input == "GO": # If they want to continue to check their status
        age = int(ask_age())
        driver_license = ask_driver_license()
        if age < 16: # If the user is too young
            print("You are too young, go back to school. ")
        elif age < 18: # If the user can drive but not drink
            print("You can not legally drink, but your mates/uncles might have your back (bigger 16).")
            if age >= 17 and driver_license:
                print("You can drive.")
        else: # if the user can drive and vote
            if driver_license:
                print("You can vote and drive.")
            else:
                print("You can vote.")
    else:
        print("Try again...")
