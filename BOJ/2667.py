n = int(input())
info = []
graph = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0 #단지갯수
flag = [[-1, 0],[0, 1], [1, 0], [0, -1]]

def bfs(i, j):
  global cnt
  stack = [[i,j]]
  graph[i][j]=cnt
  visited = []
  while stack:
    el = stack.pop()
    visited.append(el)
    i, j = el[0], el[1]
    for f in range(4):
      target_i = i+flag[f][0]
      target_j = j+flag[f][1]
      if 0<= target_i and target_i < n and 0<=target_j and target_j < n and info[target_i][target_j]=='1' and graph[target_i][target_j] == 0:
        stack.append([target_i, target_j])
        graph[target_i][target_j] = cnt

  return len(visited)

for _ in range(n):
  info.append(list(input()))

#info = input().split() 테스트용

cnt_house = []
for i in range(n):
  for j in range(n):
    if info[i][j]=='1' and graph[i][j] == 0:
      cnt += 1
      cnt_house.append(bfs(i, j))


#for i in range(n):
#  print(' '.join(info[i]))
#print()
#for i in range(n):
#  print(' '.join(map(str,graph[i])))
#print()

print(cnt)
for c in sorted(cnt_house):
  print(c)
