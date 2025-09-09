RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
LIGHT_BLUE = "\033[1;34m"
CYAN = "\033[36m"


# User Profile
dp = {
    "athlete": {"age": 25, "weight": 75, "goal": "muscle gain"},
    "student": {"age": 20, "weight": 65, "goal": "healthy eating"},
    "elderly": {"age": 60, "weight": 70, "goal": "weight maintenance"}
}

# Particular User Mate.
def userprofile():
    
    print(f"{YELLOW}{BOLD}=============Choose a profile or create a custom one============={RESET}")
    print(f"{CYAN}1. Athlete (Age: 25, Weight: 75kg, Goal: Muscle Gain){RESET}")
    print(f"{CYAN}2. Student (Age: 20, Weight: 65kg, Goal: Healthy Eating){RESET}")
    print(f"{CYAN}3. Elderly (Age: 60, Weight: 70kg, Goal: Weight Maintenance){RESET}")
    print(f"{CYAN}4. Custom Profile.{RESET}")

    choice = input(f"{YELLOW}Enter your choice (1-4) : {RESET}")

    if choice in ["1", "2", "3"]:
        profiles = ["athlete", "student", "elderly"]
        profile = dp[profiles[int(choice) - 1]]
    else:
        age = input(f"{YELLOW}Enter your age : {RESET}").strip()
        weight = input(f"{YELLOW}Enter your weight (kg) : {RESET}").strip()
        goal = input(f"{YELLOW}Enter your goal (e.g., weight loss, muscle gain, healthy eating) : {RESET}").strip()
        profile = {"age": int(age), "weight": int(weight), "goal": goal}

    User_profile = open("user_personalization.txt","w")
    User_profile.write(f"{profile['age']}|{profile['weight']}|{profile['goal']}")

    print(f"\n{GREEN}Profile saved successfully!{RESET}")
    return profile


# User Profile Jova Mate.
def loadprofile():
    try:
        User_profile = open("user_personalization.txt","r")
        data = User_profile.readline().strip().split("|")
        if(data):
            print(f"{YELLOW}User Profile Loaded : {RESET}")
            print(f"{LIGHT_BLUE}Age :  {data[0]}, Weight :  {data[1]}kg, Goal : {data[2]} {RESET}")
            return {"age": int(data[0]), "weight": int(data[1]), "goal": data[2]}
        else:
            print(f"{RED}No user profile found. Let's set one up!{RESET}")
    except FileNotFoundError:
        print(f"{RED}User Profile not found! Create Profile First.{RESET}")
