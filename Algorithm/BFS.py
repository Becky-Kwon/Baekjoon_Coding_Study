# BFS 기본 구현 예제
# BFS와 DFS의 가장 큰 차이점은 While문 다음에 어떤 자료를 우선적으로 추출하느냐 입니다.
# DFS 같은 경우 리스트의 가장 끝에 있는 데이터를 기준으로 추출하지만,
# BFS는 리스트의 가장 처음에 있는 인자를 받습니다.

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']


def bfs(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)

    while need_visited:
        node = need_visited[0]
        del need_visited[0]

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

print(bfs(graph, 'A'))    # ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']

