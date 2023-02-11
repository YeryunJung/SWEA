T = int(input())
for test_case in range(1, T + 1):
  N = int(input())
  lst = list(map(int, input()))
  ans = cnt = 0
  
  for i in range(N):
    if lst[i] == 0:
      cnt = 0
    else:
      cnt += 1
      if ans < cnt:  # 연속한 최대 개수 찾기
        ans = cnt
  
  print(f'#{test_case}', ans)
