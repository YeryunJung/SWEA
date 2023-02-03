T = int(input())
for test_case in range(1, T + 1):
    total = int(input())
    carrot_lst = list(map(int, input().split()))

    sequence = [[1]*total for _ in range(2)]
    for i in range(1, len(carrot_lst)):
        if carrot_lst[i] >= carrot_lst[i - 1]:
            sequence[0][i] = sequence[0][i - 1] + 1

    max_num = max(map(max, sequence))
    print(f'#{test_case} {max_num}')
