# 백준 - 1260

n, m, start = map(int, input().split())
data = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    data[s].append(e)
    data[e].append(s)

# 정렬 (번호가 작은 노드 부터 방문)
for i in range(n+1):
    data[i].sort()


def dfs(node):
    print(node, end=' ')
    visited[node] = True
    for a in data[node]:
        if not visited[a]:
            dfs(a)

visited = [False]*(n+1)
dfs(start)
print()

def bfs(node):
    que_list = []
    que_list.append(node)
    visited[node] = True
    while que_list:
        now_node = que_list[0]
        del que_list[0]
        print(now_node, end=' ')
        for b in data[now_node]:
            if not visited[b]:
                visited[b] = True
                que_list.append(b)


visited = [False]*(n+1)
bfs(start)