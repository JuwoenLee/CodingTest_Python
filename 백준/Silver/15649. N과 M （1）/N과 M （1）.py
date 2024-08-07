import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numList = []

def dfs() :
    if len(numList) == M :
        print((' ').join(map(str, numList)))

    for i in range(1, N + 1) : # 1 ~ N까지
        if i not in numList : # i가 리스트에 없는 숫자라면
            numList.append(i) # 리스트에 추가
            dfs() # 반복문의 다음 숫자 계산 & 길이 확인( + 출력)
            numList.pop() # 맨 뒤 숫자 제거로 다른 배열 생성 가능성 확인

dfs()