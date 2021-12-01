T = int(input())
for i in range(T):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  R = ((x1-x2)**2 + (y1-y2)**2) **0.5
  if R == 0 and r1 == r2: #일치하는 경우
    print(-1)
  elif r1 + r2 == R or abs(r1-r2) == R: #한점에서 만나는 경우
    print(1)
  elif abs(r1-r2) < R < r1 + r2: #두점에서 만나는 경우
    print(2)
  else: #만나지 않는 경우
    print(0)
