import sys

try:
    flag = True
    cardsets = []
    datasets = []
    counter = 0
    while True:
        data = int(sys.stdin.readline())
        if data == 0:
            break
        for i in range(2):
            cardsets.append(map(str, sys.stdin.readline().split()))
        datasets.append(cardsets)

except (ValueError, IndexError):
    sys.stdout.write("DOES NOT EXIST " + '\n')
    exit()

weights = {}
weights["A"] = 20
weights["2"] = 2
weights["3"] = 3
weights["4"] = 4
weights["5"] = 5
weights["6"] = 6
weights["7"] = 7
weights["8"] = 8
weights["9"] = 9
weights["T"] = 10
weights["J"] = 15
weights["Q"] = 15
weights["K"] = 15
weights["R"] = 50

for item in datasets:

    b1 = item[0]
    b2 = item[1]
    sum = 0
    if "R" in b1 and "R" in b2:
        b3 = [val for val in b1 if val in b2]
        for item in b3:
            sum += weights[item]*2
    elif "R" not in b1 and "R" not in b2:
        b3 = [val for val in b1 if val in b2]
        for item in b3:
            sum += weights[item]*2
    else:
        inb1 = b1.count("R")
        inb2 = b2.count("R")
        if inb1 > 0:
            filter(lambda a: a == "R", b1)
        if inb2 > 0:
            filter(lambda a: a != "R", b2)
        b3 = [val for val in b1 if val in b2]
        for item in b3:
            sum += weights[item]*2
    print sum