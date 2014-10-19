import sys

try:
    data = map(int, sys.stdin.readline().split())
except ValueError:
    sys.stdout.write("NO" + '\n')
    exit()

if not data:
    sys.stdout.write("NO" + '\n')
    exit()

if len(data) != 2:
    sys.stdout.write("NO" + '\n')
    exit()

if data[0] < 1 or data[0] > 1000:
    sys.stdout.write("NO" + '\n')
    exit()

if data[1] < 0 or data[1] > 100000:
    sys.stdout.write("NO" + '\n')
    exit()

if data[1] == 0:
    sys.stdout.write("YES" + '\n')
    exit()

constraints = []
try:
    for i in range(data[1]):
        constraints.append(map(int, sys.stdin.readline().split()))
        if sum(1 for number in constraints[i] if number > data[0] or number < 1) > 0:
            sys.stdout.write("NO" + '\n')
            exit()
except ValueError:
    sys.stdout.write("NO" + '\n')
    exit()

studyplan = []
try:
    studyplan = map(int, sys.stdin.readline().split())
    if sum(1 for number in studyplan if number > data[0] or number < 1) > 0:
            sys.stdout.write("NO" + '\n')
            exit()
except ValueError:
    sys.stdout.write("NO" + '\n')
    exit()


for item in constraints:
    for i in range(len(item)):
        for j in range(i+1, len(item)):
            if item[i] in studyplan and item[j] in studyplan:
                if studyplan.index(item[i]) > studyplan.index(item[j]):
                    sys.stdout.write("NO" + '\n')
                    exit()

sys.stdout.write("YES" + '\n')