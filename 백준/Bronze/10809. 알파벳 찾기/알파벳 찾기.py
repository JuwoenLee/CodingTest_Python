S = input()
lower_alpha = [-1] * 26

for i in range(len(S)) :
    if lower_alpha[ord(S[i]) - 97] == -1 :
        lower_alpha[ord(S[i]) - 97] = i

print(*lower_alpha)