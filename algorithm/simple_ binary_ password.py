T = int(input())
for tc in range(1, T + 1):
    password = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }
 
    # 암호 가로길이는 56
    # 배열 세로크기 N, 가로크기 M
    N, M = map(int, input().split())
    board = [list(map(int, input())) for _ in range(N)]
    arr = []
 
    for lst in board:
        if 1 in lst:
            arr = list(map(str, lst))
            break
 
    idx = 0
    for i in range(0, len(arr)-6):
        if ''.join(arr[i:i + 7]) in password:
            idx = i
            break
 
    # 암호를 돌면서 8자리 숫자가 모두 나올 때까지 잘라서 확인
    nums = []
    i = 0
    while len(nums) != 8:
        slicing_arr = arr[idx:idx + 56]
        for i in range(0, len(slicing_arr)-6, 7):
            temp = ''.join(slicing_arr[i:i + 7])
            if temp in password:
                nums.append(password[temp])
                i += 7
            elif temp not in password:
                idx += 1
                nums = []
                break
 
    even = odd = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            even += nums[i]
        else:
            odd += nums[i]
 
    result = 0
    if ((even * 3) + odd) % 10 == 0:
        result = sum(nums)
 
    print(f'#{tc}', result)
