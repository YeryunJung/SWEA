T = int(input())
for test_case in range(1, T + 1):
    total = int(input())
    arr = list(map(int, input().split()))

        # 마지막 인덱스에서부터 버블정렬
    for i in range(total - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

        # 정렬된 리스트에서 가장 큰 수(맨 뒤)에서 가장 작은 수(맨 앞) 빼기
    result = arr[-1] - arr[0]
    print(f'#{test_case} {result}')