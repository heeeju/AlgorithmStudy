days = [31,28,31,30,31,30,31,31,30,31,30,31]
info = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())
answer = 0

for i in range(0, x-1):
  answer += days[i]

answer += y

print(info[answer%7])
