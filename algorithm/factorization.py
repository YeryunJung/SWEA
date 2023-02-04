T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    argu = [2, 3, 5, 7, 11]
    lst = [0] * 5
    for i in range(len(argu)):
        while num % argu[i] == 0:
            lst[i] += 1
            num = num // argu[i]
             
    result = " ".join(map(str, lst))
    print(f'#{tc} {result}')
