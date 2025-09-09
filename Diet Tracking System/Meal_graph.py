import matplotlib.pyplot as plt

def meal_graph(username):
	t_meal = []
	t_calorie = []
	file =f"Meal_Plan_{username}.txt"
	food_log = open(file,"r")
	for line in food_log:
		data = line.strip().split("|")
		t_meal.append(data[0])
		t_calorie.append(int(float(data[1])))

	print(t_meal)
	print(t_calorie)

	x = t_meal
	y = t_calorie

	plt.title(f"{username.capitalize()} Graph")
	plt.pie(y,labels = x,radius = 1.0,autopct = "%0.2f%%",wedgeprops = {"linewidth":1, "edgecolor":"red"})
	plt.legend(loc=1)
	plt.show()