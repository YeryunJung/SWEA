# 제일 오래 걸리는 방법
"""
모든 시작점에서 k를 넓혀가면서 전체 순회
"""
cost = [((k*k) + (k-1)*(k-1)) for k in range(40)]
# def solve_loop():
#     mx = 0
#     for si in range(N):  # 가능한 모든 시작위치
#         for sj in range(N):
#             for k in range(1, 2 * N): # 서비스 영역의 크기 k 안에서
#                 cnt = 0
#                 for i in range(si-k+1, si+k):  # 마름모 행의 시작과 끝 행
#                     t = abs(si - i)
#                     for j in range(sj-k+1+t, sj+k-t):
#                         if 0 <= i < N and 0 <= j < N:
#                             # 집위치 더하기
#                             cnt += arr[i][j]  # 집이 아니면 0이 더해짐, 집이면 1
#
#                 # 운영비용보다 수익이 같거나 큰 경우 정답갱신
#                 # if ((k*k)+(k-1)*(k-1)) <= cnt*M:
#                 if cost[k] <= cnt * M:
#                     mx = max(mx, cnt)
#     return mx

#################################################################
# bfs로 푸는 방법
"""
bfs 4방향, 범위내, 미방문 cnt += 1
v[ci][cj] 변경될 때 정답갱신
"""
def bfs(si, sj):
    q = []
    v = [[0]*N for _ in range(N)]
    old = 0  # 플래그
    mx = 0

    q.append((si, sj))  # 초기 데이터 삽입
    v[si][sj] = 1  # 초기 데이터 방문 표시
    cnt = arr[si][sj]  # 시작 좌표가 집이면 1, 아니면 0 이걸 그대로 써준다

    while q:
        ci, cj = q.pop(0)
        if old != v[ci][cj]:  # k값이 달라진 경우
            old = v[ci][cj]  # 사용한 플래그를 기존값하고 바꿔줘야 한다 (사실상 k값)
            if cost[v[ci][cj]] <= cnt*M:
                mx = max(mx, cnt)  # 정답 갱신

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj]==0:  # 함수 범위 내 미방문 했다면
                q.append((ni, nj))  # nexti nextj
                v[ni][nj] = v[ci][cj] + 1
                cnt += arr[ni][nj]  # 변경될 때 > 이전값과 달라졌는지 쓰는 것

    return mx

def solve_bfs():
    mx = 0
    for si in range(N):
        for sj in range(N):  # 가능한 모든 시작위치에서 bfs 실행
            mx = max(mx, bfs(si, sj)) # 호출해서 리턴하는 것 중에 큰 값
    return mx


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N은 도시의 크기, M은 가구당 지불비용
    arr = [list(map(int, input().split())) for _ in range(N)]

    # ans = solve_loop()
    ans = solve_bfs()
    print(f'#{tc}', ans)
#################################################################
# 범위 기준 표시후 확산 => 집 기준 접근! (범위는 넓고 집은 조금일 때)
# [1] 집 좌표를 저장
# [2] 각 기준위치에서 집 거리를 표시(누적)
# dist = [0, 2, 0, 5, .....] 40개의 배열 (누적합)
# cost[k] <= dist[k] * M


# 그리디하게 푸는 방법

def solve_idea():
    mx = 0
    home = []
    for si in range(N):  # 전체를 순회하면서
        for sj in range(N):
            if arr[si][sj] == 1:  # 집이 있으면
                home.append((si, sj))  # [1] 홈 배열에 집의 모든 위치를 저장

    # [2] 모든 좌표 순회하면서, dist 배열 만들고(거리별 집의 개수 누적), cnt 처리
    for si in range(N):
        for sj in range(N):
            dist = [0] * 40
            # 거리별 집위치를 누적
            for ti, tj in home:
                # k가 3이면 거리가 2인 애들까지만 집을 구하니까 (자기자신일 때 k가 1이니까 거리에 자기자신인 1을 더해줌)
                t = abs(si-ti) + abs(sj-tj) + 1  # 시작위치에서 집의 위치 빼면 나와의 거리, 다 빼서 같은 위치라도 1?
                dist[t] += 1  # 예를 들어 dist 배열의 3의 위치에 집 한채 추가

            for k in range(1, 40):  # 40이 최대범위
                dist[k] = dist[k - 1]  # 누적
                if cost[k] <= dist[k] * M:  # 여태까지 비용이 누적 집의 개수 * 내는 돈보다 작다면 갱신
                    mx = max(mx, dist[k])
    return mx
