# 나눠서 떨어지면 인수

T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    argu = [2, 3, 5, 7, 11]
    lst = [0] * 5
    
    for i in range(len(argu)):
        while num % argu[i] == 0:  # 나누어 떨어지는 경우
            lst[i] += 1  # 개수 추가
            num = num // argu[i]  # 나눠서 재할당
             
    reuslt = " ".join(map(str, lst))
    print(f'#{tc} {result}')
