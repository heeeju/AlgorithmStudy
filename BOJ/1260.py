from collections import deque
info = {}
n, m, v = map(int, input().split())

def DFS():
  visited = []
  stack = [v]
  while stack:
    target = stack.pop()
    if target not in visited:
      visited.append(target)
      if target in info:
        stack += sorted(list(set(info[target]) - set(visited)), reverse = True)

  return map(str, visited)

def BFS():
  visited = []
  queue = deque([v])
  while queue:
    target = queue.popleft()
    if target not in visited:
      visited.append(target)
      if target in info:
        queue += sorted(list(set(info[target]) -set(visited)))

  return map(str, visited)

for _ in range(m):
  s, e = map(int, input().split())
  if s not in info:
    info[s] = [e]
  else:
    info[s].append(e)

  if e not in info:
    info[e] = [s]
  else:
    info[e].append(s)

print(' '.join(DFS()))
print(' '.join(BFS()))
