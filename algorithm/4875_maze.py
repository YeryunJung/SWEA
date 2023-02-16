def dfs(x, y):
    while stack:
        x, y = stack.pop()
        visited[x][y] = 1

    for d in range(4):
        x1 = x + dx[d]
        y1 = y + dy[d]
        if 0 <= x1 < size and 0 <= y1 < size and maze[x1][y1] == 0 and visited[x1][y1] == 0:
            stack.append([x1, y1])
            visited[x1][y1] = 1
            dfs(x1, y1)
        elif 0 <= x1 < size and 0 <= y1 < size and maze[x1][y1] == 3:
            global switch
            switch = 1


    return switch


T = int(input())
for tc in range(1, T + 1):
    size = int(input())
    maze = [list(map(int, input())) for _ in range(size)]
    visited = [[0]*size for _ in range(size)]

    # X = Y = 0
    for i in range(5):
        for j in range(5):
            if maze[i][j] == 2:
                X = i
                Y = j

    visited[X][Y] = 1
    stack = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    switch = 0


    dfs(X,Y)
    print(f'#{tc}', switch)
