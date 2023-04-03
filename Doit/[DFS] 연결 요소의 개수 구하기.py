# 백준 11742

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
print(graph)
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
print(graph)

result = 0
for j in range(1, n+1):
    if not visited[j]:
        result += 1
        dfs(j)
print(result)


