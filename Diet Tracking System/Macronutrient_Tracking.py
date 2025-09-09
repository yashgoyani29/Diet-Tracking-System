RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
PURPLE = "\033[0;35m"
LIGHT_BLUE = "\033[1;34m"
CYAN = "\033[36m"

# Food dictionary with calorie values per serving
foodcalorie = {
    # Fruits
    "apple": 95,  
    "banana": 105,
    "orange": 62, 
    "grapes": 69, 
    "mango": 200, 
    "strawberry": 50,  
    "watermelon": 85,  
    "pineapple": 82,  
    "blueberry": 85,
    
    # Vegetables
    "carrot": 25,  
    "potato": 110,  
    "tomato": 22,  
    "broccoli": 55,  
    "onion": 44,  
    
    # Dairy
    "milk": 150,
    "cheese": 113,
    "butter": 102,
    "yogurt": 100, 
    
    # Meat & Poultry
    "chicken breast": 165,
    "beef": 250,
    "pork": 242,
    "fish": 206,
    "egg": 70,
    
    # Grains & Breads
    "rice": 200,
    "bread": 80,
    "pasta": 220,
    "oats": 150,
    
    # Beverages
    "coffee": 2,
    "tea": 1,
    "soda": 150,
    
    # Snacks & Fast Food
    "chocolate": 220,
    "chips": 152,
    "pizza": 285,
    "burger": 295,
}


# Log a food entry with serving-based calorie calculation
def logfooditem():
    print(f"\n{CYAN}Log a New Food Item{RESET}")
    date = input(f"{YELLOW}Enter date (YYYY-MM-DD) : {RESET}").strip()
    foodname = input(f"{YELLOW}Enter food name : {RESET}").lower().strip()
    quantity = float(input(f"{YELLOW}Enter quantity (number of servings) : {RESET}"))

    if foodname in foodcalorie:
        calories = foodcalorie[foodname]
    else:
        calories = float(input(f"{YELLOW}Enter calories manually : {RESET}"))
        foodcalorie[foodname] = calories

    protein = float(input(f"{YELLOW}Enter protein (g) : {RESET}"))
    carbs = float(input(f"{YELLOW}Enter carbs (g) : {RESET}"))
    fats = float(input(f"{YELLOW}Enter fats (g) : {RESET}"))

    entry = f"{date}|{foodname}|{quantity}|{calories:.2f}|{protein}|{carbs}|{fats}\n"
    food_log = open("food_log.txt","a")
    food_log.write(entry)

    print(f"{GREEN}Food item logged successfully!{RESET}")

# Calculate total daily intake
def calculatedailyintake():
    print(f"\n{CYAN}Calculate Daily Intake{RESET}") 
    date = input(f"{YELLOW}Enter date (YYYY-MM-DD) : {RESET}").strip()

    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fats = 0
    found = False

    try:
        food_log = open("food_log.txt","r")
        for line in food_log:
            data = line.strip().split("|")
            if data[0] == date:
                found = True
                _,foodname,quantity,calories, protein, carbs, fats = data
                total_calories += float(calories)*float(quantity)
                total_protein += float(protein)*float(quantity)
                total_carbs += float(carbs)*float(quantity)
                total_fats += float(fats)*float(quantity)

        entry = f"{date}|{foodname}|{quantity}|{total_calories:.2f}|{total_protein}|{total_carbs}|{total_fats}\n"
        food_log_total = open("food_log_total.txt","a")
        food_log_total.write(entry)

        print(f"{GREEN}Food item logged successfully!{RESET}")

        if found:
            print(f"{CYAN}\nTotal Intake for {date}:{RESET}")
            print(f"-{LIGHT_BLUE} Calories: {total_calories:.2f} kcal{RESET}")
            print(f"-{LIGHT_BLUE} Protein: {total_protein:.2f} g{RESET}")
            print(f"-{LIGHT_BLUE} Carbohydrates: {total_carbs:.2f} g{RESET}")
            print(f"-{LIGHT_BLUE} Fats: {total_fats:.2f} g{RESET}")
        else:
            print(f"{RED}Enter Correct date!{RESET}")

    except FileNotFoundError:
        print(f"{RED}Food log file not found! Start by logging a food item.{RESET}")

# View all food logs
def viewfoodlog():
    print(f"\n{YELLOW}{BOLD}Food Log Entries : {RESET}")
    try:
        food_log = open("food_log.txt","r")
        entries = food_log.readlines()
        if not entries:
            print(f"{RED}No food entries logged yet!{RESET}")
        else:
            for entry in entries:
                data = entry.strip().split("|")
                date, food_name, quantity, calories, protein, carbs, fats = data
                print(f"{YELLOW}{date}: {food_name} ({quantity} servings) - {calories} cal, Protein: {protein}g, Carbs: {carbs}g, Fats: {fats}g {RESET}")
    except FileNotFoundError:
        print(f"{RED}No food log file found! Start by logging a food item.{RESET}")

# Main menu
def main_menu():
    while True:
        print(f"{PURPLE}1. Log Food Item{RESET}")
        print(f"{PURPLE}2. View Food Log{RESET}")
        print(f"{PURPLE}3. Calculate Daily Intake{RESET}")
        print(f"{PURPLE}4. Exit{RESET}")
        choice = input(f"{YELLOW}Enter your choice : {RESET}")

        if choice == "1":
            logfooditem()
        elif choice == "2":
            viewfoodlog()
        elif choice == "3":
            calculatedailyintake()
        elif choice == "4":
            print(f"{YELLOW}Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")