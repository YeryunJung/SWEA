T = int(input())

for test_case in range(1, T+1):
    total, num = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_list = []
    last_idx = total - num + 1
    
        # num 개씩 묶은 합을 sum_list에 추가
    for i in range(last_idx):
        sum = 0
        for j in range(i, i + num):
            sum += arr[j]
        sum_list.append(sum)
    
        # sum_list에서 가장 큰 수와 가장 작은 수 찾기
    max = sum_list[0]
    min = sum_list[0]
    for sum in sum_list:
        if sum > max:
            max = sum
        if sum < min:
            min = sum
    
    print(f'#{test_case} {max - min}')