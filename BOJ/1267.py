n = int(input())
call = list(map(int, input().split()))
y = 0
m = 0

for c in call:
  y += (c // 30 + 1) * 10
  m += (c // 60 + 1) * 15

if y > m:
  print("M", end=' ')
elif m > y:
  print("Y", end=' ')
else:
  print("Y M", end=' ')

print(min(y, m))
