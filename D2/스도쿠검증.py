import sys
sys.stdin = open("./input/sdocu.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 안겹치면 1, 겹치면 0
for test_case in range(1, T + 1):
  def unique(el):
      if len(set(el)) == len(el):
          return True
      else:
          return False

  result = 1
  two_dimension = [list(map(int, input().split())) for _ in range(9)]
  for el in two_dimension:
    if unique(el) == True:
      continue
    else:
      result = 0
  print('#%d' % test_case, result)