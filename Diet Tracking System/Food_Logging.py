RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"


Food_logs = {}

# Enter Food 
def logfood(username):
    print(f"\n{CYAN}--- Log Food ---{RESET}")
    foodname = input(f"{YELLOW}Enter the food name : {RESET}").strip()
    quantity = input(f"{YELLOW}Enter quantity (e.g., '1 cup') : {RESET}").strip()
    calories = input(f"{YELLOW}Enter calories : {RESET}").strip()
    protein = input(f"{YELLOW}Enter protein (g) : {RESET}").strip()
    carbs = input(f"{YELLOW}Enter carbs (g) : {RESET}").strip()
    fats = input(f"{YELLOW}Enter fats (g) : {RESET}").strip()

    if username not in Food_logs:
        Food_logs[username] = []  

    Food_logs[username].append({
        "foodname": foodname,
        "quantity": quantity,
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fats": fats
    })

    print(f"{GREEN}Food logged successfully!{RESET}")

# View food.
def viewfood(username):
    print(f"\n{CYAN}--- Food Log for {BOLD}{username}{RESET}{CYAN} ---{RESET}")
    if username not in Food_logs or not Food_logs[username]:
        print(f"{YELLOW}No food logged yet.{RESET}")
        return

    print(f"{BOLD}Food Name{RESET} \t| {BOLD}Quntatity{RESET} \t| {BOLD}Calories{RESET} \t| {BOLD}Protien{RESET} \t| {BOLD}Carbs{RESET} \t| {BOLD}Fats{RESET}")
    
    print(f"{'-' * 100}")
    for entry in Food_logs[username]:
        print(f"{entry['foodname']: <15} | {entry['quantity']: <10} \t| {entry['calories']: <8} \t| {entry['protein']: <7} \t| {entry['carbs']: <6} \t| {entry['fats']: <5}")
    print(f"{'-' * 100}")
