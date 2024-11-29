n = int(input())
m = 1234567891
string = input()
trans = [ord(string[i]) - 96 for i in range(n)]
result = [trans[i] * pow(31, i) for i in range(n)]

print(sum(result) % m)