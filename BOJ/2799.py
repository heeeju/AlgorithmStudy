row, col = map(int, input().split())

info = []
cnt = [0,0,0,0,0]
for _ in range(row * 5 +1):
  info.append(input())

for r in range(1, row * 5 + 1, 5):
  for c in range(1, col * 5 + 1, 5):
    cnt_star = 0
    for i in range(4):
      if info[r+i][c]=='*':
        cnt_star+=1
    cnt[cnt_star] += 1

for i in range(5):
  print(cnt[i], end=' ')
