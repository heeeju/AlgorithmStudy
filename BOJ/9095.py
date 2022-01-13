stack = []
cnt = 0

def dfs(n):
  global cnt
  all = sum(stack)
  if all == n:
    cnt += 1
    return
  elif all > n:
    return
  else:
    stack.append(1)
    dfs(n)
    stack.pop()
    stack.append(2)
    dfs(n)
    stack.pop()
    stack.append(3)
    dfs(n)
    stack.pop()


n = int(input())
for _ in range(n):
  stack = []
  cnt = 0
  num = int(input())
  dfs(num)
  print(cnt)
