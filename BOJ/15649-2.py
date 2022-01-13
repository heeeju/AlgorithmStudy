n, m = map(int, input().split())
nums = []

def dfs():
  if len(nums) == m:
    print(' '.join(map(str, nums)))
    return
  for i in range(1,n+1):
    if i not in nums:
      nums.append(i)
      dfs()
      nums.pop()

dfs()
