n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

t_shirt = 0

if t == 1:
    t_shirt = sum(1 for s in size if s > 0)
else:
    for s in size:
        if s == 0 :
            continue
        if s <= t:
            t_shirt += 1
        else:
            t_shirt += (s + t - 1) // t

print(t_shirt)
print(n // p, n % p)