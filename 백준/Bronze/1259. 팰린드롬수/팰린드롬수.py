while True :
    n = input()
    
    if n == '0' :
        break

    else :
        answer = 'yes'
        for i in range(len(n) // 2) :
            if n[i] == n[-(i + 1)] :
                continue

            else :
                answer = 'no'
                break
        print(answer)