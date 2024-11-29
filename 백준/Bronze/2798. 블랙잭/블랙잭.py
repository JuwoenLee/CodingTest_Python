n, m = map(int, input().split())
cards = list(map(int, input().split()))
total = []

for i in cards :
    for j in cards[cards.index(i) + 1 : ] :
        for k in cards[cards.index(j) + 1 : ] :
            if (i + j + k) <= m :
                total.append(i + j + k)

print(max(total))