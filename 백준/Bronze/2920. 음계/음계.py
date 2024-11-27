sound = list(map(int, input().split()))

c_major = [i for i in range(1, 9)]

if sound == c_major :
    print("ascending")

elif sound == sorted(c_major, reverse=True) :
    print("descending")

else :
    print("mixed")