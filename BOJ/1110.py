n = int(input())
cycle = 0
num = n

while cycle == 0 or n != num:
  one = num//10
  two = num%10
  add = (one+two) % 10
  num = int(str(two)+str(add))
  cycle += 1

print(cycle)
