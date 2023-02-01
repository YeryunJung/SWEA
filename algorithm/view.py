T=10
for test_case in range(1, T + 1):
    total = int(input())
    arr = list(map(int, input().split()))
    light_view = 0
        # 0 0 이 아닌 부분의 요소를 순회하면서
    for i in range(2, total - 2):
        max = 0
                # 이전 빌딩 2개와 이후 빌딩 2개 중 가장 높은 빌딩 탐색 후 max에 할당
        for j in range(i - 2, i):
            if arr[j] > max:
                max = arr[j]
        for k in range(i + 1, i + 3):
            if arr[k] > max:
                max = arr[k]
                # 현재 요소가 가장 높은 빌딩이면 내 높이에서 max 뺀 값의 합을 출력 
        if arr[i] > max:
            light_view += arr[i] - max
    print(f'#{test_case} {light_view}')