n, k = map(int, input().split())
nums = []
for _ in range(n):
  nums.append(int(input()))

cnt = 0
for num in nums[::-1]:
  cnt += k // num
  k %= num

print(cnt)
