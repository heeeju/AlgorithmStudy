import collections
n = int(input())
names = [input() for i in range(n)]
names_f = [n[0] for n in names]

count = collections.Counter(names_f)
answer = ''

for k,v in zip(count.keys(), count.values()):
  if v >= 5:
    answer += k

if len(answer) == 0:
  print('PREDAJA')
else:
  print(''.join(sorted(answer)))
