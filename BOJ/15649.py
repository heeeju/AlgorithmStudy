from itertools import permutations

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
answer = permutations(nums,m)

for a in answer:
  for i in range(len(a)):
    print(a[i], end=' ')
  print()
