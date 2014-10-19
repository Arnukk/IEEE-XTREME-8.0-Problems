import sys
import math


def twosquares(n):
    if n < 2:
        return False
    else:
        for i in range(1, n):
            for j in range(i+1, n):
                if math.pow(i, 2) + math.pow(j, 2) == math.pow(n, 2):
                    return True
                    break
        return False


try:
    data = int(sys.stdin.readline())
except ValueError:
    sys.stdout.write("FALSE" + '\n')
    exit()


if not data:
    sys.stdout.write("FALSE" + '\n')
    exit()

if data < 0 or data > 10:
    sys.stdout.write("FALSE" + '\n')
    exit()

if data == 0:
    sys.stdout.write("FALSE" + '\n')
    exit()

triangles = []
try:
    for i in range(data):
        triangles.append(map(int, sys.stdin.readline().split()))
        if len(triangles[i]) != 2:
            sys.stdout.write("FALSE" + '\n')
            exit()
        if sum(1 for number in triangles[i] if number < 0 or number > 1000) > 0:
            sys.stdout.write("FALSE" + '\n')
            exit()
except ValueError:
    sys.stdout.write("FALSE" + '\n')
    exit()


for item in triangles:
    flag = True
    for i in item:
        if not twosquares(i):
            flag = False
            sys.stdout.write("FALSE" + '\n')
            break
    if flag:
        sys.stdout.write("TRUE" + '\n')