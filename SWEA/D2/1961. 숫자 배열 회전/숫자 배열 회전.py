def rotate(matrix) :
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            rotated_matrix[j][n - i - 1] = matrix[i][j]
    return rotated_matrix

T = int(input())

for test_case in range(1, T + 1) :
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    rotated_90 = rotate(arr)
    rotated_180 = rotate(rotated_90)
    rotated_270 = rotate(rotated_180)

    print(f"#{test_case}")
    for i in range(n) :
        print(''.join(str(r) for r in rotated_90[i]), end=' ')
        print(''.join(str(r) for r in rotated_180[i]), end=' ')
        print(''.join(str(r) for r in rotated_270[i]))