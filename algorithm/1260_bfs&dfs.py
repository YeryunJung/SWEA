def dfs(v):
    dfs_check[v] = True
    print(v, end=' ')

    # 모든 요소를 돌면서
    for i in range(1, N + 1):
        # 방문하지 않았고 현재 정점과 연결되어 있는 정점
        if not dfs_check[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    # 큐 생성
    q = [v]
    # 현재 노드 방문 처리
    bfs_check[v] = True
    # 큐가 빌때까지 반복
    while q:
        # 큐에서 하나의 원소를 뽑아 추력
        ci = q.pop(0)
        print(ci, end=' ')
        # 모든 정점을 돌면서
        for i in range(1, N + 1):
            # 해당 원소와 연결되고 아직 방문하지 않은 원소들을 큐에 삽입
            if not bfs_check[i] and graph[ci][i] == 1:
                q.append(i)
                bfs_check[i] = True

# 정점 개수 N, 간선 개수 M, 시작 정점 번호 V
N, M, V = map(int, input().split())
node = {}
dfs_check = [False for _ in range(N + 1)]
bfs_check = [False for _ in range(N + 1)]
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    n, v = map(int, input().split())
    graph[n][v] = graph[v][n] = 1

dfs(V)
print()
bfs(V)
