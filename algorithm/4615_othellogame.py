"""
범위 체크를 줄이고 싶으면 주변에 0, -1, 1 이런식으로 패딩을 주기
1. 초기모양 배치
2. arr[si][sj] = d 초기 위치에 놓기
    - 8방향
    - 뻗어나가면서
    arr[ni][nj] 다음좌표가
    0: break 0 이면 아무것도 안한다 뻗어나갈 필요가 없다
    다른 돌: 뒤집힐 후보 templist에 좌표를 추가 (바로 뒤집진 못한다)
    같은 돌: templist 후보들 뒤집기
3.
"""

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # arr 네 방향 패딩해서 둘러쌈
    arr = [[0]*(N+2) for _ in range(N + 2)]
    # [1] 초기 돌 위치 놓기
    m = N // 2
    arr[m][m] = arr[m+1][m+1] = 2
    arr[m+1][m] = arr[m][m+1] = 1

    # [2] 흑돌 백돌 입력 받아서 처리
    for _ in range(M):
        si, sj, color = map(int, input().split())
        arr[si][sj] = color
        # 8방향 처리
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            # 해당 방향으로 뻗어나가면서 처리
            # N 전까지
            tlst = [] # 임시로 넣어놓는 스택
            for mul in range(1, N): # 한 쪽 방향으로 어디까지 검사할 것인지
                ni, nj = si + di*mul, sj+dj*mul
                if arr[ni][nj] == 0: # 빈칸이나 범위 밖에 부딪히면 (예를 들어 위쪽으로 끝났다면 29번째 줄 for 문으로 나가서 대각선 방향으로 벽에 부딪힐 때가지 검사)
                    break
                elif arr[ni][nj] != color: # 다른 돌인 경우 뒤집기 후보에 추가
                    tlst.append((ni, nj))
                else: # 같은 돌 => 후보 들을 뒤집고, 종료
                    while tlst:
                        ti, tj = tlst.pop()
                        arr[ti][tj] = color # 뒤집는다 같은 돌을 준다
                    break

    blackcnt = whitecnt = 0
    for lst in arr:
        blackcnt += lst.count(1)
        whitecnt += lst.count(2)
    print(f'#{tc} {blackcnt} {whitecnt}')
