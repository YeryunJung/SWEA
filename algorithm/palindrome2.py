T = 10
for test_case in range(1, T + 1):
    length = int(input())
    # 가로 추출
    row_arr = [input() for _ in range(int(8))]
 
    # 세로 추출
    col_arr = ['' for _ in range(8)]
    for i in row_arr:
        for j in range(8):
            col_arr[j] += i[j]
 
    # 회문 판별
    def is_pal(arr):
        cnt = 0
        for i in range(8):
            for j in range(8):
                # 범위 내에 존재 / 시작글자와 마지막글자 동일 / 뒤집어도 동일
                if 0 <= j + length <= 8 and (arr[i][j] == arr[i][j+length-1]) and (arr[i][j:j+length] == arr[i][j:j+length][::-1]):
                    cnt += 1
        return cnt
 
    print(f'#{test_case} {is_pal(row_arr) + is_pal(col_arr)}')
