n = int(input())
v = int(input())
graph = {}
def DFS():
  visited = []
  root = 1
  stack = [root]

  while stack:
    t = stack.pop()
    if t not in visited:
      visited.append(t)
      if t in graph:
        stack += list(set(graph[t]) - set(visited))

  return len(visited)-1

for _ in range(v):
  s, e = map(int, input().split())
  if s not in graph:
    graph[s] = [e]
  else:
    graph[s].append(e)
  if e not in graph:
    graph[e] = [s]
  else:
    graph[e].append(s)

print(DFS())
