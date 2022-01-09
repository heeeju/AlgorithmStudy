n = int(input())
info = []
for _ in range(n):
  w, h = map(int, input().split())
  info.append([w, h])

for i in range(n):
  cnt = 1
  for j in range(n):
    if j != i and info[i][0] < info[j][0] and info[i][1] < info[j][1]:
      cnt += 1
  print(cnt, end = ' ')
