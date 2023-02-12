# 배열 범위 내 체크를 하지 않으려면 좌, 우에 패딩을 줘야 한다
# 좌우를 0으로 감싼다
# 정답 좌표에서 ans - 1 해야겠다

# 좌 / 우 : 1순위!
# 좌 / 우가 아니면 직진
# dj [-1, 1, 0] # 좌우하

# 진행 방향대로 가다가 방향이 있으면 방향대로 간다 (모든 것)
# 1 ~ 100까지
# si <- 0, sj(1인 지점), cnt, ci, cj

# while ci < 99:  # 99가 되면 멈춰야 한다 100이 아니라
#     if dj == 0:  # 아래 방향이면 좌 우 체크가 먼저
#         if arr[ci][cj - 1] == 1: # 좌
#             dj = -1  # 방향 좌로 변경
#             cj -= 1
#         elif arr[ci][cj + 1] == 1: # 우
#             dj = 1 # 방향 우로 변경
#             cj += 1
#         else:  # 아래
#             ci += 1
#
#     else: # 좌 / 우 방향이라면 => 직진
#         if arr[ci][cj + dj] == 1: # 진행방향 1이면
#             cj += dj # 그대로 좌우로 직진
#         else: # 방향이 바뀌는 것
#             dj = 0
#             ci += 1
#
#     if mn >= cnt # 정답 갱신
#         mn, ans = cnt, sj - 1


T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    mn = 100*100 # 일단 크게 해서 갱신되도록
    for sj in range(1, 101): # (좌표의 열)
        # [1] 시작 지점 찾기
        si = 0 # si는 안바뀌니까 (시작좌표의 행)
        if arr[si][sj] != 1: # 1이 아니면 시작 안함
            continue
        cnt, dj = 0, 0
        ci, cj = si, sj
        while ci < 99:  # 99가 되면 멈춰야 한다 100이 아니라
            cnt += 1
            if dj == 0:  # 아래 방향이면 좌 우 체크가 먼저
                if arr[ci][cj - 1] == 1:  # 좌
                    dj = -1  # 방향 좌로 변경
                    cj -= 1
                elif arr[ci][cj + 1] == 1:  # 우
                    dj = 1  # 방향 우로 변경
                    cj += 1
                else:  # 아래
                    ci += 1
            else:  # 좌 / 우 방향이라면 => 직진
                if arr[ci][cj + dj] == 1:  # 진행방향 1이면
                    cj += dj  # 그대로 좌우로 직진
                else:  # 방향이 바뀌는 것
                    dj = 0
                    ci += 1
        if cnt <= mn : # 복수의 경우에 가장 큰 거라 = 붙여줌
            mn, ans = cnt, sj - 1

    print(f'#{test_case} {ans}')

    # if와 else를 내 진행 방향대로 정하는게 중요하다

