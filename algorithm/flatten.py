T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    count = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    while arr[-1] - arr[0] > 1:
        arr[-1] -= 1
        arr[0] += 1
        count -= 1
        # 정렬이 깨졌다면
        if arr[-1] <= arr[-2] or arr[0] <= arr[1]:
            arr.sort()
        if count == 0:
            break

    print(arr[-1] - arr[0])
