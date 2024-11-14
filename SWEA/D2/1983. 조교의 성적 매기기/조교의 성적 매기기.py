T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_case in range(1, T + 1) :
    n, k = map(int,input().split())
    maxNum = n // 10
    total = dict()

    for i in range(n) :
        mid, final, assignment = map(float, input().split())
        total[mid * 0.35 + final * 0.45 + assignment * 0.2] = i + 1

    sorted_total = sorted(total.items(), reverse=True)

    idx = 0
    for t_key, t_value in sorted_total :    
        if t_value == k :
            break
        idx += 1
        

    print("#{} {}".format(test_case, grade[idx // maxNum]))