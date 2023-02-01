T=int(input())
for test_case in range(1, T + 1):
    total = int(input())
    arr = list(map(int, input().split()))
    ans = 0

        # 리스트를 순회하면서
    for i in range(total):
        cnt = 0
                # 현재 요소보다 이후에 있는 요소들 중에 나보다 작은 값이 있으면
                # count ++
        for j in range(i + 1, total):
            if arr[i] > arr[j]:
                cnt += 1

                # count 중에 가장 큰 수 출력
        ans = max(cnt, ans)
    print(f'#{test_case} {ans}')