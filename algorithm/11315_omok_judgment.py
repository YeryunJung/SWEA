def bfs(x, y):
    global result
    q = [(x, y)]

    while q:
        ci, cj = q.pop(0)
        for i in range(8):
            cnt = 0
            for j in range(1, 5):
                ni = ci + di[i] * j
                nj = cj + dj[i] * j
                # 돌이 없으면 빠져나오게
                if 0 <= ni < N and 0 <= nj < N:
                    if board[ni][nj] != 'o':
                        break
                # 돌이 있으면
                    elif board[ni][nj] == 'o':
                        cnt += 1
                        if cnt >= 4:
                            return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = 0
    board = [list(input()) for _ in range(N)]
    # 좌상대각선, 위, 우상대각선, 좌, 우, 좌하대각선, 하, 우하대각선
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    result = 0
    switch = True

    for i in range(len(board)):
        if not switch:
            break
        for j in range(len(board)):
            if not switch:
                break
            if board[i][j] == 'o':
                result = bfs(i, j)
                if result == 'YES':
                    switch = False

    print(f'#{tc}', result)
