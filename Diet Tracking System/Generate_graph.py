import matplotlib.pyplot as plt

def show_graph():
	t_date = []
	t_calorie = []
	food_log = open("food_log_total.txt","r")
	for line in food_log:
		data = line.strip().split("|")
		t_date.append(data[0])
		t_calorie.append(int(float(data[3])))

	t_date.insert(0, t_date[0])
	t_calorie.insert(0, 0)
	print(t_date)
	print(t_calorie)

	x = t_date
	y = t_calorie

	plt.xlabel("Date",fontsize=15)
	plt.ylabel("Calorie",fontsize=15)
	plt.title("Daily Diet Track Report", fontsize=20)

	plt.bar(x, y, width = 0.3, color = "green", label="Date")
	plt.xticks(rotation = 45)
	plt.legend()
	plt.show()