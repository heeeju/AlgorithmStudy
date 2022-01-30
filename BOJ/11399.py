n = int(input())
times = sorted(list(map(int, input().split())))

cur = 0
answer = 0
for t in times:
  cur += t
  answer += cur

print(answer)
