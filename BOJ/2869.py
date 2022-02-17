a, b, v = map(int, input().split())

left = v - a
answer = 1

answer += left // (a-b) +1

if left % (a-b) == 0:
  answer -= 1

print(answer)
