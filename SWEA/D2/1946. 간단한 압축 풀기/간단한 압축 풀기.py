T = int(input())

for test_case in range(1, T + 1) :
    n = int(input())
    alphabet_string = ""

    for _ in range(n) :
        alphabet, repeat = input().split()
        alphabet_string += alphabet * int(repeat)

    print(f"#{test_case}")
    while(alphabet_string != "") :
        print(alphabet_string[:10])
        alphabet_string = alphabet_string[10 : ]