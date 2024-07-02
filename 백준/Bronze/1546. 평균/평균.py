n = int(input())
scores = input().split(' ')
scores = list(map(int, scores))
total = sum(scores)
max_score = max(scores)

print(total / max_score * 100 / n)