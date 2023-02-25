T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    # 슬라이딩 윈도우로 풀이
    k = len(str1)
    result = 0
    # 윈도우 생성
    window = str2[:k]
    if window == str1: result = 1
    for i in range(k, len(str2)):
        window += str2[i]
        # 맨 처음 발견되는 앞 문자만 삭제
        window = window.replace(str2[i - k], '', 1)
        # 문자열을 포함한다면 순회 종료
        if window == str1:
            result = 1
            break

    print(f'#{tc}', result)
