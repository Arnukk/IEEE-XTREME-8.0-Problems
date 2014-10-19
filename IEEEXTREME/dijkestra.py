from collections import defaultdict
import heapq
import sys

try:
    def dijkstra(edges, f, t):
        g = defaultdict(list)
        for l,r,c in edges:
            g[l].append((c,r))

        q, seen = [(0,f,())], set()
        while q:
            (cost,v1,path) = heapq.heappop(q)
            if v1 not in seen:
                seen.add(v1)
                path = (v1, path)
                if v1 == t:
                    return cost#(cost, path)
                for c, v2 in g.get(v1, ()):
                    if v2 not in seen:
                        heapq.heappush(q, (cost+c, v2, path))

        return float("inf")

    try:
        linesqty = int(sys.stdin.readline())
    except ValueError:
        sys.stdout.write(str(0) + '\n')
        exit()

    if not linesqty or linesqty < 1 or linesqty > 1000:
        sys.stdout.write(str(0) + '\n')
        exit()

    matrix = [0]*linesqty
    try:
        for i in range(linesqty):
            matrix[i] = map(int, sys.stdin.readline().split())
            if sum(1 for number in matrix[i] if number > 1000000) > 0:
                sys.stdout.write(str(0) + '\n')
                exit()
            if sum(1 for number in matrix[i] if number < 0) > 0:
                sys.stdout.write(str(0) + '\n')
                exit()
            if len(matrix[i]) != linesqty:
                sys.stdout.write(str(0) + '\n')
                exit()
            matrix[i].append(0)
    except (ValueError, IndexError, RuntimeError):
        sys.stdout.write(str(0) + '\n')
        exit()

    A = matrix

    edges = []

    for i in range(len(A)):
        for j in range(len(A[0])):
            if i > 0:
                if j != len(A[0])-1:
                    edges.append((str(i)+str(j), str(i-1)+str(j), A[i][j]))
            if i < len(A)-1:
                if j != len(A[0])-1:
                    edges.append((str(i)+str(j), str(i+1)+str(j), A[i][j]))
            if j < len(A[0])-1:
                edges.append((str(i)+str(j), str(i)+str(j+1), A[i][j]))



    mincosts = []
    for i in range(len(A)):
        for j in range(len(A)):
            mincosts.append(dijkstra(edges, str(i) + str(0), str(j)+ str(len(A[0])-1)))

    if not mincosts:
        sys.stdout.write(str(0) + '\n')
        exit()
    else:
        sys.stdout.write(str(min(mincosts)) + '\n')
except RuntimeError:
    sys.stdout.write(str(0) + '\n')