import sys
import operator

class Voyager:

    def __init__(self, Fuel, Distances, Costs, Capacity):
        self.Fuel = Fuel
        self.Distances = Distances
        self.Costs = Costs
        self.Passed = 0
        self.Capacity = Capacity
        self.Expenses = 0

    def update(self, Fuel, diff, index):
        self.Fuel = Fuel
        del self.Distances[index]
        del self.Costs[index]
        for i in range(len(self.Distances)):
                self.Distances[i] = self.Distances[i] - diff
        self.Distances = filter(lambda x: x >= 0, self.Distances)
        self.Passed += diff



def isreachablecheapest(Fuel, stationsdist, stationscost, Refill, Stranger):
    if not Refill:
        available = []
        for i in range(len(stationsdist)):
            if Fuel >= stationsdist[i]:
                available.append((stationsdist[i], stationscost[i], i))
        sorted_by_second = sorted(available, key=lambda tup: tup[1])
        return sorted_by_second[0]
    else:
        global r
        global t
        print t
        available = []
        for i in range(len(stationsdist)):
                available.append((stationsdist[i], stationscost[i], i))
        sorted_by_second = sorted(available, key=lambda tup: tup[1])
        for j in sorted_by_second:
            if Stranger.Capacity >= int(j[0]):
                thetemp = Stranger.Fuel
                Stranger.Fuel = int(j[0])
                Stranger.Expenses += (int(j[0]) - thetemp) * int(t[r])
                print Stranger.Expenses
                return j

try:
    data = int(sys.stdin.readline())
except ValueError:
    sys.stdout.write("-1" + '\n')
    exit()

NFTL = []
try:
    for i in range(data):
        NFTL = map(int, sys.stdin.readline().split())
except ValueError:
    sys.stdout.write("-1" + '\n')
    exit()


stationsdist = []
stationscost = []
try:
    for i in range(NFTL[0]):
        temp = sys.stdin.readline().split()
        stationsdist.append(int(temp[0]))
        stationscost.append(int(temp[1]))
except ValueError:
    sys.stdout.write("-1" + '\n')
    exit()


def voyage(TheVoyager, Refill, toPass):
    if not TheVoyager.Distances:
        TheVoyager.Fuel += toPass - TheVoyager.Passed - TheVoyager.Fuel
        TheVoyager.Expenses += TheVoyager.Fuel * TheVoyager.Costs[-1]
        TheVoyager.Passed += TheVoyager.Fuel
        return TheVoyager.Expenses, TheVoyager.Passed
    thedestination = isreachablecheapest(TheVoyager.Fuel, TheVoyager.Distances, TheVoyager.Costs, Refill, TheVoyager)
    global r
    r = int(thedestination[2])
    TheVoyager.update(TheVoyager.Fuel - int(thedestination[0]), int(thedestination[0]), int(thedestination[2]))
    return voyage(TheVoyager, True, toPass)




global t
t = stationscost


MyVoyager = Voyager(NFTL[2], stationsdist, stationscost, NFTL[1])
print voyage(MyVoyager, False, NFTL[3])



