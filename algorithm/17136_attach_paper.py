# 최소 개수를 붙여야 하니까 가장 큰 색종이부터 부착 시도
def put_paper(x, y):
    flag = False
    size = 0
    for k in range(5, 0, -1):
        if flag:
            for m in range(x, x + k):
                for n in range(y, y + k):
                    my_board[m][n] = 1
            return k
        # # 아무것도 맞는 색종이가 없었으면
        # else:
        #     return -1

        # if flag:
        #     flag = False
        # else:
        #     size = k
        #     break
        for i in range(x, x + k):
            # 색종이가 맞지 않아서 끝낸다 > 더 작은 색종이를 붙인다
            if flag:
                break
            for j in range(y, y + k):
                # 색종이가 맞지 않으면 끝낸다 > 더 작은 색종이를 붙인다
                if board[i][j] != 1:
                    flag = True
                    break
            # 색종이 크기가 맞았다면
            else:
                flag = False
    # 색종이가 맞았으면
    # if not flag:
    #     for m in range(x, x + size):
    #         for n in range(y, y + size):
    #             my_board[m][n] = 1
    #     return size
    # # 아무것도 맞는 색종이가 없었으면
    # else:
    #     return -1


board = [list(map(int, input().split())) for _ in range(10)]
my_board = [[0] * 10 for _ in range(10)]

result = []
for i in range(10):
    for j in range(10):
        # 색종이 붙일 자리가 있고 이미 붙이지 않았다면
        if board[i][j] == 1 and my_board[i][j] != 1:
            result.append(put_paper(i, j))

print(result)
