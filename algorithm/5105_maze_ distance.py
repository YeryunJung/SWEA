def bfs(v, w):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append([v, w])
    visited[v][w] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.pop(0) # q의 첫번째 원소 반환
        for k in range(4):
            xi = x + dx[k]
            yi = y + dy[k]
            if 0 <= xi < N and 0 <= yi < N and visited[xi][yi] == 0:
                if maze[xi][yi] == 3:
                    return visited[x][y]
                if maze[xi][yi] == 0:
                    q.append([xi, yi])
                    visited[xi][yi] = visited[x][y] + 1
    return 0
 
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
 
    x = y = 0
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 2:
                x, y = i, j
 
    result = bfs(x, y)
    print(f'#{tc}', result)
