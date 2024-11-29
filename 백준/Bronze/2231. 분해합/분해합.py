n = int(input())
result = 0

for i in range(1, n + 1) :
    value = i
    chr = str(i)

    for c in chr :
        value += int(c)
    
    if value == n :
        result = i
        break

print(result)