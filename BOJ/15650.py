from itertools import combinations

n, m = map(int, input().split())
arr = [i+1 for i in range(n)]

cbns = combinations(arr, m)

for cbn in list(cbns):
  for el in cbn:
    print(el, end = ' ')
  print()
