T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    floor = [[i for i in range(1, n + 2)]]

    for i in range(1, k + 1):
        ifloor = [sum(floor[i - 1][:j + 1]) for j in range(n + 1)]
        floor.append(ifloor)

    print(floor[k][n - 1])