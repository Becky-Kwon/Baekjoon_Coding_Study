# DFS 기본 구현 예제
# md 파일 속 사진 참고
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

print(graph)

# "스택/큐"를 활용한 DFS 구현

# [참고]
# list.append(x)는 리스트 끝에 x 1개를 그대로 넣습니다.
# list.extend(iterable)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣습니다.


# - (1) 리스트를 활용한 DFS 구현
def dfs_list(graph, start_node):
    ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, visited = list(), list()
    ## 시작 노드를 시정하기
    need_visited.append(start_node)

    ## 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visited:
        ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visited.pop()
        ## 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
            ## 방문한 목록에 추가하기
            visited.append(node)
            ## 그 노드에 연결된 노드를
            need_visited.extend(graph[node])
    return visited
print(dfs_list(graph, 'A'))    # ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']

# - (2) deque를 활용한 DFS 구현
def dfs_deque(graph, start_node):
    ## deque 패키지 불러오기
    from collections import deque
    visited = []
    need_visited = deque()
    ##시작 노드 설정해주기
    need_visited.append(start_node)

    ## 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        ## 시작 노드를 지정하고
        node = need_visited.pop()

        ##만약 방문한 리스트에 없다면
        if node not in visited:
            ## 방문 리스트에 노드를 추가
            visited.append(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
    return visited
print(dfs_deque(graph, 'A'))   # ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']


# "재귀함수"를 활용한 DFS 구현
def dfs_recursive(graph, start, visited=[]):
    ## 데이터를 추가하는 명령어 / 재귀가 이루어짐
    visited.append(start)

    for node in graph[start]:
        print('node', node)
        print('visited', visited)
        if node not in visited:
            dfs_recursive(graph, node, visited)

    return visited

print(dfs_recursive(graph, 'A', visited=[]))   # ['A', 'B', 'D', 'E', 'F', 'C', 'G', 'H', 'I', 'J']







