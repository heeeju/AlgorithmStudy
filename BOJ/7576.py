from collections import deque

m, n = map(int, input().split())
t_info = []
queue = deque([])
zeros = []
minus = []
day = 0
check = 1


for i in range(n):
  t = list(map(int, input().split()))
  t_info.append(t)
  for j in range(m):
    if t[j] == 1:
      queue.append([i,j, 0])
    elif t[j] == 0:
      zeros.append([i,j])

if len(zeros) == 0:
  print(0)
  check = 0

if check :
  while queue:
    i, j, d = queue.popleft()
    day = d #depth

    if 0<= i-1 and t_info[i-1][j] == 0:
      t_info[i-1][j] = 1
      queue.append([i-1, j, d+1])

    if i+1 < n and t_info[i+1][j] == 0:
      t_info[i+1][j] = 1
      queue.append([i+1, j, d+1])

    if 0<= j-1 and t_info[i][j-1] == 0:
      t_info[i][j-1] = 1
      queue.append([i,j-1, d+1])

    if j+1 < m and t_info[i][j+1] == 0:
      t_info[i][j+1] = 1
      queue.append([i, j+1, d+1])

  for t in t_info:
    if 0 in t:
      day = -1
      break
  print(day)
