import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
S = list()

for i in range(1, N) :
    ip, iv = i, P[i]

    while ip > 0 and P[ip - 1] > iv :
        P[ip] = P[ip - 1]
        ip -= 1
    P[ip] = iv

S.append(P[0])

preSum = 0
total = 0

for value in P :
    preSum += value
    total += preSum

print(total)