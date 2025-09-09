'''
    Enrollment No : 23002170210035
    Date : 28/02/2025
    Subject : FCSP-1
'''
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
LIGHT_BLUE = "\033[1;34m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

from Food_Logging import *
from Macronutrient_Tracking import *
from User_Personalization import * 
from Meal_Planning import *
from Generate_graph import *

Calorie_goal = {}
Calorie_log = {}

# Password Validator
def validatepassword(password):
    if len(password) <= 8:
        return False

    upper = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in "$_@" for c in password)

    return upper and digit and special

# Load Users In File.
def loadusers():
    users = {}
    try:
        file = open("userdetails.txt","r")
        for line in file:
            username, password = line.strip().split(":-")
            users[username] = password        
    except FileNotFoundError:
        users = {}
    return users

# Write Users In File.
def saveusers(users):
    file = open("userdetails.txt","w")
    for username, password in users.items():
        file.write(f"{username}:-{password}\n")

# Register a New User.
def registeruser():
    users = loadusers()

    print(f"\n{CYAN}--- Register ---{RESET}")
    username = input(f"{YELLOW}Enter a username: {RESET}").strip()
    
    if username in users:
        print(f"{RED}Error: Username already exists. Please choose a different one.{RESET}")
        return False

    while True:
        password = input(f"{YELLOW}Enter a password: {RESET}").strip()

        if validatepassword(password):
            print(f"{GREEN}Valid Password{RESET}")
            break
        else:
            print(f"{RED}Invalid Password.{RESET}")

    confirmpassword = input(f"{CYAN}Confirm your password: {RESET}").strip()
    
    if password != confirmpassword:
        print(f"{RED}Error: Passwords do not match. Please try again.{RESET}")
        return False

    users[username] = password
    Calorie_log[username] = []
    saveusers(users)
    print(f"{GREEN}Registration successful! You can now log in.{RESET}")
    return True

# Log In An Existing User.
def loginuser():
    users = loadusers()
    print(f"\n{CYAN}--- Login ---{RESET}")
    username = input(f"{YELLOW}Enter your username: {RESET}").strip()
    
    if username not in users:
        print(f"{RED}Error: Username not found. Please register first.{RESET}")
        return None
    
    password = input(f"{YELLOW}Enter your password: {RESET}").strip()
    
    if users[username] == password:
        print(f"{GREEN}Login successful! Welcome back, {BOLD}{username}{RESET}!")
        return username
    else:
        print(f"{RED}Error: Incorrect password. Please try again.{RESET}")
        return None

# Log Calories
def logcalories(username):
    try:
        calories = int(input(f"{YELLOW}Enter calories consumed: {RESET}"))
        if username not in Calorie_log:
            Calorie_log[username] = []
        Calorie_log[username].append(calories)
        print(f"{GREEN}Calories logged successfully!{RESET}")
    except ValueError:
        print(f"{RED}Error: Please enter a valid number.{RESET}")

# Set Calorie Goal
def setcaloriegoal(username):
    try:
        goal = int(input(f"{YELLOW}Enter your daily calorie goal: {RESET}"))
        Calorie_goal[username] = goal
        print(f"{GREEN}Calorie goal set successfully!{RESET}")
    except ValueError:
        print(f"{RED}Error: Please enter a valid number.{RESET}")

# View Calorie Intake
def viewcalories(username):
    totalcalories = sum(Calorie_log.get(username, []))
    print(f"{CYAN}Total Calories Consumed: {BOLD}{totalcalories}{RESET}")
    if username in Calorie_goal:
        remaining = Calorie_goal[username] - totalcalories
        print(f"{CYAN}Remaining Calories for the day: {BOLD}{remaining}{RESET}")
    else:
        print(f"{YELLOW}No calorie goal set. Use 'Set Calorie Goal' to define your target.{RESET}")
######################################################################################################
# Main Method
def main():
    while True:
        print(f"\n{YELLOW}{BOLD}--- Diet Tracking System ---{RESET}")
        print(f"{CYAN}1. Register{RESET}")
        print(f"{CYAN}2. Login{RESET}")
        print(f"{CYAN}3. Exit{RESET}")

        choice = input(f"{CYAN}========Choose an option========{RESET}\n").strip()
        
        if choice == "1":
            registeruser()
        elif choice == "2":
            username = loginuser()
            if username:
                while True:
                    print(f"\n{YELLOW}{BOLD}--- Welcome, {username}! ---{RESET}")
                    print(f"{CYAN}1. Log Food{RESET}")
                    print(f"{CYAN}2. View Food Log{RESET}")
                    print(f"{CYAN}3. Log Calories{RESET}")
                    print(f"{CYAN}4. Set Calorie Goal{RESET}")
                    print(f"{CYAN}5. View Calorie Intake{RESET}")
                    print(f"{CYAN}6. Macronutrient Tracking{RESET}")
                    print(f"{CYAN}7. User Personalization{RESET}")
                    print(f"{CYAN}8. Meal Plannig{RESET}")
                    print(f"{CYAN}9. Daily Diet Track{RESET}")
                    print(f"{CYAN}10. Logout{RESET}")

                    schoice = input(f"{CYAN}Choose an option: {RESET}").strip()
                    
                    if schoice == "1":
                        logfood(username)
                    elif schoice == "2":
                        viewfood(username)
                    elif schoice == "3":
                        logcalories(username)
                    elif schoice == "4":
                        setcaloriegoal(username)
                    elif schoice == "5":
                        viewcalories(username)
                    elif schoice == "6":
                        main_menu()
                    elif schoice == "7":
                        userprofile()
                        loadprofile()
                    elif schoice == "8":
                        user_menu(username)
                    elif schoice == "9":
                        show_graph()
                    elif schoice == "10":
                        print(f"{YELLOW}Logged out. Returning to main menu.{RESET}")
                        break
                    else:
                        print(f"{RED}Invalid choice. Please try again.{RESET}")
        elif choice == "3":
            print(f"{YELLOW}Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")

######################################################################################################
main()
