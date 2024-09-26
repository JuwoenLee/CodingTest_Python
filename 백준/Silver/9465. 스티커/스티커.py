# 높이가 n인 정수 삼각형이 주어졌을 때,
# 맨 위층부터 아래 있는 수 중 하나를 선택하여 (대각선 좌, 우만 선택 가능)
# 선택된 수들의 합 중 최댓값을 출력하는 프로그램

import sys
input = sys.stdin.readline

for _ in range(int(input())) :

    n = int(input())
    
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    # dp 첫번째 열 저장
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    # 스티커의 길이가 1이면
    if n == 1 :
        # 둘 중 큰 값을 출력
        print(max(dp[0][0], dp[1][0]))
        # 다음 테스트케이스 진행
        continue

    # 스티커의 길이가 2 이상이면
    dp[0][1] = dp[1][0] + sticker[0][1]
    dp[1][1] = dp[0][0] + sticker[1][1]

    # 스티커의 길이가 2이면
    if n == 2 :
        # 둘 중 큰 값을 출력
        print(max(dp[0][1], dp[1][1]))
        # 다음 테스트케이스 진행
        continue

    # 2 ~ (n - 1)까지 최대합 계산
    for i in range(2, n) :
        # 직전 열의 값을 더하지 않을 수 있음 => i - 2, i - 1를 비교해서 dp 업데이트
        # 윗 줄 계산
        dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + sticker[0][i]
        # 아래 줄 계산
        dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + sticker[1][i]

    # dp 중 최댓값 출력
    print(max(dp[0][-1], dp[1][-1]))