# [1] cnts[] 빈도수 배열에 빈도수 표시 (N개)
# [2] 지정된 정류장 버스 개수 입력
# alst = [] 정답 리스트에 append(cnts[p])

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # N번 반복하면서 노선입력, 빈도수 표시

    cnts = [0] * 5001 # 5000개니까 5001개 배열 생성
    for _ in range(N):
        S, E = map(int, input().split())
        for i in range(S, E + 1):  # start 부터 end까지
            cnts[i] += 1  # count 배열에 빈도수를 표시

    P = int(input())  # 정류장 개수
    alst = []
    for _ in range(P):  # P번 반복
        p = int(input())
        alst.append(cnts[p])  # p 안에 있는 것을 추가 
        
    result = " ".join(map(str, alst))
    print(f'#{test_case} {result}')
    # print(f'#{test_case}', *alst)
