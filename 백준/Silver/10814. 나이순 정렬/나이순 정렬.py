import sys
input = sys.stdin.readline

n = int(input())
members = list()

for i in range(n) :
    members.append(input().split())

members = sorted(members, key = lambda x: int(x[0]))

for member in members :
    print(*member)