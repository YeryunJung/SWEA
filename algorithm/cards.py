T = int(input())
for test_case in range(1, T + 1):
    total = int(input())
    arr = list(map(int, input()))
    
    # 각 카드의 개수를 구하는 카운팅 배열 생성
    c = [0] * 10
    for i in range(len(arr)):
        c[arr[i]] += 1
        
    # 카운팅 배열을 순회하면서 
    # 개수가 같거나 크고 카드 넘버가 가장 큰 요소를 구해서 출력
    max_count = max_card = 0
    for idx, count in enumerate(c):
        if count >= max_count and idx > max_card:
            max_count = count
            max_card = idx
            
    print(f'#{test_case} {max_card} {max_count}')
