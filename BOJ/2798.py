from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0

cases = combinations(cards, 3)
for case in cases:
  case_sum = sum(list(case))
  if answer < case_sum <= m:
    answer = case_sum

print(answer)
