import sys

data = map(str, sys.stdin.readline().split())

if not data:
    sys.stdout.write("The total calorie intake is " + str(0) + '\n')
    exit()

try:
    int(data[0])
except ValueError:
    sys.stdout.write("The total calorie intake is " + str(0) + '\n')
    exit()

pizzaseaten = [0] * int(data[0])
data.pop(0)
if not data:
    sys.stdout.write("The total calorie intake is " + str(0) + '\n')
    exit()
qty = []
supplements = []
try:
    for i in range(len(pizzaseaten)):
        if int(data[i*2]) != 0:
            qty.append(int(data[i*2]))
            supplements.append(data[i*2+1].split(","))
except (ValueError, IndexError):
    sys.stdout.write("The total calorie intake is " + str(0) + '\n')
    exit()

suppcalories = {}
suppcalories["Anchovies"] = 50
suppcalories["Artichoke"] = 60
suppcalories["Bacon"] = 92
suppcalories["Broccoli"] = 24
suppcalories["Cheese"] = 80
suppcalories["Chicken"] = 30
suppcalories["Feta"] = 99
suppcalories["Garlic"] = 8
suppcalories["Ham"] = 46
suppcalories["Jalapeno"] = 5
suppcalories["Meatballs"] = 120
suppcalories["Mushrooms"] = 11
suppcalories["Olives"] = 25
suppcalories["Onions"] = 11
suppcalories["Pepperoni"] = 80
suppcalories["Peppers"] = 6
suppcalories["Pineapple"] = 21
suppcalories["Ricotta"] = 108
suppcalories["Sausage"] = 115
suppcalories["Spinach"] = 18
suppcalories["Tomatoes"] = 14


overallcalories = 0
for i in range(len(qty)):
    temp = 0
    for j in supplements[i]:
        if j in suppcalories.keys():
            temp += suppcalories[j]
    overallcalories += qty[i] * (270 + temp)

sys.stdout.write("The total calorie intake is " + str(overallcalories) + '\n')

