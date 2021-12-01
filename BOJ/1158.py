N, K = map(int, input().split())
nums = [i for i in range(N)]
idx = -1
answer = '<'
while len(nums) > 0:
  idx = (idx + K) % len(nums)
  answer += (str(nums[idx]+1) + ', ')
  del nums[idx]
  idx -= 1

print(answer[:-2]+'>')
