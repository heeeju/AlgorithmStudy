n = int(input())
words = [input() for i in range(n)]

for w in sorted(list(set(words)), key = lambda x : (len(x), x)):
  print(w)
