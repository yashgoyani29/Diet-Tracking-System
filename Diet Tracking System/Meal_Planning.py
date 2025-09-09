RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
LIGHT_BLUE = "\033[1;34m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

from Meal_graph import *

# Predefined Meal List (Meal Name: {Calories, Protein, Carbs, Fats})
Mealplan = {
    "breakfast": [
        {"name": "Oatmeal with Banana", "calories": 250, "protein": 6, "carbs": 45, "fats": 3},
        {"name": "Scrambled Eggs & Toast", "calories": 320, "protein": 20, "carbs": 30, "fats": 12},
        {"name": "Greek Yogurt & Berries", "calories": 180, "protein": 15, "carbs": 25, "fats": 3}
    ],
    "lunch": [
        {"name": "Grilled Sandwich & Rice", "calories": 400, "protein": 40, "carbs": 50, "fats": 8},
        {"name": "Salmon & Quinoa", "calories": 450, "protein": 42, "carbs": 50, "fats": 10},
        {"name": "Vegetable Stir-fry", "calories": 300, "protein": 12, "carbs": 55, "fats": 5}
    ],
    "dinner": [
        {"name": "Steak & Vegetables", "calories": 500, "protein": 45, "carbs": 35, "fats": 18},
        {"name": "Lentil Soup & Bread", "calories": 350, "protein": 20, "carbs": 50, "fats": 6},
        {"name": "Brocoli soup & Salad", "calories": 380, "protein": 40, "carbs": 25, "fats": 8}
    ]
}

# Save user's meal selection to a file
def savemealplan(username, meal):
    file = f"Meal_Plan_{username}.txt"
    write_meal = open(file,"a")
    write_meal.write(f"{meal['name']}|{meal['calories']}|{meal['protein']}|{meal['carbs']}|{meal['fats']}\n")

# View saved meals for the user
def viewmealplan(username):
    file = f"Meal_Plan_{username}.txt"
    print(f"\n{CYAN}--- Meal Plan for {username} ---{RESET}")

    try:
        View_meal= open(file,"r")
        meals = View_meal.readlines()

        if not meals:
            print(f"{YELLOW}No meals selected yet.{RESET}")
            return
        total_calories, total_protein, total_carbs, total_fats = 0, 0, 0, 0
        for meal in meals:
            name, calories, protein, carbs, fats = meal.strip().split("|")
            total_calories += int(calories)
            total_protein += int(protein)
            total_carbs += int(carbs)
            total_fats += int(fats)
            print(f"{GREEN}- {name} ({calories} kcal, Protein: {protein}g, Carbs: {carbs}g, Fats: {fats}g){RESET}")


        print(f"\n{CYAN}Total Daily Intake:{RESET}")
        print(f"Calories: {total_calories} kcal")
        print(f"Protein: {total_protein}g, Carbs: {total_carbs}g, Fats: {total_fats}g")

    except FileNotFoundError:
        print(f"{YELLOW}No meal plan found. Start selecting meals!{RESET}")

# Select meals for the day
def selectmeal(username):
    print(f"\n{CYAN}--- Select Your Meals ---{RESET}")

    for mt, meals in Mealplan.items():
        print(f"\n{BOLD}{mt.capitalize()} Options:{RESET}")
        for i, meal in enumerate(meals, 1):
            print(f"{YELLOW}{i}. {meal['name']} ({meal['calories']} kcal){RESET}")

        choice = input(f"{CYAN}Choose a {mt} option (1-{len(meals)}) or press Enter to skip: {RESET}").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(meals):
            meal = meals[int(choice) - 1]
            savemealplan(username, meal)
            print(f"{GREEN}Added {meal['name']} to your meal plan!{RESET}")

# User dashboard after login
def user_menu(username):
    while True:
        print(f"\n{YELLOW}{BOLD}--- Welcome, {username}! ---{RESET}")
        print(f"{CYAN}1. Select Meals{RESET}")
        print(f"{CYAN}2. View Meal Plan{RESET}")
        print(f"{CYAN}3. User Graph{RESET}")
        print(f"{CYAN}4. Logout{RESET}")

        choice = input(f"{CYAN}Choose an option: {RESET}").strip()

        if choice == "1":
            selectmeal(username)
        elif choice == "2":
            viewmealplan(username)
        elif choice == "3":
            meal_graph(username)
        elif choice == "4":
            print(f"{YELLOW}Logging out...{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Try again.{RESET}")