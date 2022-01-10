n = int(input())
nums = list(map(int, input().split()))
stack = [[0, 100000001]]

for i, num in enumerate(nums):
  while stack[-1][1] <= num:
    stack.pop()
  print(stack[-1][0], end=' ')
  stack.append([i+1, num])
