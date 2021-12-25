L = int(input())
S = sorted([0] + list(map(int, input().split())))
N = int(input())

if N in S:
  print(0)
else:
  for i in range(len(S)-1):
    left = S[i]
    right = S[i+1]
    if N in range(left, right):
      break
  left += 1
  right -= 1
  print((right - left) + (N-left)*(right-N))
