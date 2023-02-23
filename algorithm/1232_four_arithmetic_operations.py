def postord(n): # 후위순회
    if lst[n]:
        if lst[n] == '+':
            return postord(int(left[n])) + postord(int(right[n])) # 왼쪽 트리계산 값과 오른쪽 트리 계산 값을 연산
        elif lst[n] == '-':
            return postord(int(left[n])) - postord(int(right[n]))
        elif lst[n] == '*':
            return postord(int(left[n])) * postord(int(right[n]))
        elif lst[n] == '/':
            return postord(int(left[n])) // postord(int(right[n]))
        else:
            return int(lst[n]) # 리스트 요소가 그냥 숫자면 바로 숫자 리턴
 
T = 10
for tc in range(1, T + 1):
    N = int(input())  # 정점의 개수
    lst = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    data = [input().split() for _ in range(N)]
 
    for i in data:
        idx = int(i[0])
        lst[idx] = i[1]
        if len(i) > 2: # 자식 노드에 대한 정보가 있으면 왼쪽, 오른쪽 배열에 추가해주기
            left[idx] = int(i[2])
            right[idx] = int(i[3])
 
    result = int(postord(1))
    print(f'#{tc}', result)
