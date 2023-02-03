T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # [1] N번 반복하면서 노선입력, 빈도수 표시

    cnts = [0]*5001
    for _ in range(N):
        S, E = map(int, input().split())
        for i in range(S, E + 1):
            cnts[i] += 1

    P = int(input())
    alst = []
    for _ in range(P):
        p = int(input())
        alst.append(cnts[p])
        
    result = " ".join(map(str, alst))
    print(f'#{test_case} {result}')
