T = int(input()) # 테스트 케이스
# H = 호텔의 층 수, W = 각 층의 방 수, N = 몇 번째 손님
for _ in range(T) :
    H, W, N = map(int, input().split())

    room_list = list()

    for i in range(1, W + 1) :
        for j in range(1, H + 1) :
            room_list.append((j, i))
        
    customer_room = room_list[N - 1]
    if customer_room[1] > 9 :
        print(f'{customer_room[0]}{customer_room[1]}')
    else : print(f'{customer_room[0]}0{customer_room[1]}')