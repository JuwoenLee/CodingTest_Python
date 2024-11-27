t = int(input())

for _ in range(t) :
    repeat, word = input().split()

    result = ""

    for w in word :
        result += w * int(repeat)

    print(result)