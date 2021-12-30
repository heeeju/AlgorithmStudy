def factorial(n):
  if n == 0 or n == 1:
    return 1
  idx = 1
  if num[n-1]==1:
    idx = max(idx, num.index(max(num)))
    for i in range(idx, n+1):
      num[i-1]= num[i-2] * i
  return num[n-1]

num = [1 for i in range(30)]
T = int(input())
for _ in range(T):
  n, m = map(int, input().split())
  answer = factorial(m) / (factorial(n) * factorial(m-n))
  print(int(answer))
