t = int(input())
dp = [0,1,2,4,0,0,0,0,0,0,0]
for _ in range(t):
  n = int(input())
  for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
  print(dp[n])
