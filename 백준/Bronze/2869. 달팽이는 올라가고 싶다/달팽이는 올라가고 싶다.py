A, B, V = map(int, input().split())

if A >= V :
    print(1)

else :
    distance = V - A
    move = A - B
    print((distance + move - 1) // move + 1)