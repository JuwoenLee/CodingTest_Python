n = int(input())
value = 1
dis = 0
for i in range(0, 1000000000, 6) :
    if n == 1 :
        print(1)
        break
        
    if value >= n :
        print(dis)
        break

    value += i
    dis += 1