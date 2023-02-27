def bfs(x, y):
    q = [(x, y)]
    visited[x][y] = 1

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = ci+di
            nj = cj+dj
            if 0 <= ni < 4 and 0 <= nj < 5 and island[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1

island = [list(map(int, input())) for _ in range(4)]
visited = [[0] * 5 for _ in range(4)]

cnt = 0

for i in range(4):
    for j in range(5):
				# 섬이고 방문하지 않았으면
        if island[i][j] == 1 and visited[i][j] == 0:
						# 섬 개수 추가
            cnt += 1
            bfs(i, j)

print(cnt)
