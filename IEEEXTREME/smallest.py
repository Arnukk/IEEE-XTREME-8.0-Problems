import sys
from random import choice


def rselect(seq,i):# i is the i'th order statistic.
    if len(seq)<=i:return seq
    lo,pi,hi= random_partition(seq)
    if i < len(lo):return rselect(lo,i)
    if i < len(seq)-len(hi): return pi
    return rselect(hi,i-(len(seq)-len(hi)))


def random_partition(seq):
    pi =choice(seq)
    lo=[x for x in seq if x<pi]
    hi=[x for x in seq if x>pi]
    return lo,pi,hi


try:
    data = list(map(int, sys.stdin.readline().split()))
except ValueError:
    sys.stdout.write(str(0) + '\n')
    exit()

numbers = []
try:
    numbers.extend(map(int, sys.stdin.readline().split()))
    if len(numbers) != data[0]:
        sys.stdout.write(str(0) + '\n')
        exit()
except (ValueError, IndexError):
    sys.stdout.write(str(0) + '\n')
    exit()


print
exit()
if data[0] - data[1] + 1 < data[0]:
    sys.stdout.write(str(rselect(numbers, data[2]-1)) + '\n')
else:
    
    for i in range(data[1]):
        numbers.append(numbers[i])

subsequences = []
for i in range(data[0]):
    temp = []
    for j in range(i, i+data[1]):
        temp.append(numbers[j])
    subsequences.append(temp)

minimumes = []
for item in subsequences:

    #for i in range(data[2]-1):
        #index = item.index(min(item))
        #del item[index]
    minimumes.append(rselect(item, data[2]-1))

sys.stdout.write(str(min(minimumes)) + '\n')


