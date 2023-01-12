T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
a = list(map(int, input().split()))
a.sort()
b, c = divmod(T, 2)
result = a[b + c - 1]
print(result)
