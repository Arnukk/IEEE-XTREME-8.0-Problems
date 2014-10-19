import sys
import itertools



try:
    data = map(int, sys.stdin.readline().split())
except ValueError:
    sys.stdout.write("DOES NOT EXIST " + '\n')
    exit()


numbers = []
try:
    for i in range(data[3]):
        numbers.append(sys.stdin.readline().split())
except (ValueError, IndexError):
    sys.stdout.write("DOES NOT EXIST " + '\n')
    exit()

try:
    sequence = []
    for number in numbers:
        for i in range(data[0], data[1]+1):
            if number[0] in str(i):
                sequence.append(i)
except (ValueError, IndexError):
    sys.stdout.write("DOES NOT EXIST " + '\n')
    exit()

others = list(itertools.permutations(numbers))

for i in range(len(others)):
    temp = []
    for j in others[i]:
        temp += j
    others[i] = ''.join(str(elem) for elem in temp)


for other in others:
    for i in range(data[0], data[1]+1):
        if other in str(i):
            sequence.append(i)

sequence = sorted(sequence)
try:
    sys.stdout.write(str(sequence[data[2]-1]) + '\n')
except (IndexError, ValueError):
    sys.stdout.write("DOES NOT EXIST " + '\n')
