from collections import deque
from sys import stdin

def dfs():
  global n, m, info, depth
  visited = []
  stack = deque([[0,0,1]])
  while stack:
    el = stack.popleft()
    i, j, d = el[0], el[1], el[2]
    if i==(n-1) and j==(m-1):
      depth.append(d)
    if [i,j] not in visited:
      visited.append([i, j])
      #위
      if 0 <= i-1 and info[i-1][j] == 1:
        stack.append([i-1, j, d+1])
      #아래
      if i+1 < n and info[i+1][j] == 1:
        stack.append([i+1, j, d+1])
      #왼쪽
      if 0<= j-1 and info[i][j-1] == 1:
        stack.append([i, j-1, d+1])
      #오른쪽
      if j+1 < m and info[i][j+1] == 1:
        stack.append([i, j+1, d+1])

n, m = map(int, input().split())

info = []
depth = []

for _ in range(n):
  info.append(list(map(int, list(input().strip()))))

dfs()
print(min(depth))
