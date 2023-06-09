# Algorithm Study


기본 알고리즘을 이해하고, 관련된 쉬운 예제를 풀어본다.



## 브루트포스(Brute-force search)
- 설명 :  "무차별 대입 검색"이라는 의미 그대로, 무차별적으로 가능한 모든 경우의 수를 시도해 보는 알고리즘이자, 가장 순진한 알고리즘 접근법 (예를 들어, 비밀번호 4자리 자물쇠가 있다고 하면, 0000부터 9999까지 전체를 다 확인하는 것!)
- 공부 일자 : 2023.3.29

## DFS (Depth First Search, 깊이 우선 탐색)
- 설명 : 시작 노드에서 출발하여 탐색할 한 쪽 분기를 정하여 최대 깊이가지 탐색을 마친 후 다른 쪽 분기로 이동하여 다시 탐색을 수행하는 알고리즘
- 기능 : 그래프 완전 탐색
- 특징 : 재귀함수로 구현, 스택(Stack) 자료구조 이용
- 시간 복잡도 : O(V+E) 노드 수:V, 에지 수:E
- 공부 일자 : 2023.4.3

## BFS (Breadth First Search, 너비 우선 탐색)
- 설명 : 시작 노드에서 출발하여 시작 노드를 기준으로 가까운 노드를 우선하여 탐색하는 알고리즘
- 기능 : 그래프 완전 탐색
- 특징 : FIFO 탐색, 큐(Queue) 자료구조 이용
- 시간 복잡도 : O(V+E) 노드 수:V, 에지 수:E
- 공부 일자 : 2023.4.3

![](https://images.velog.io/images/513sojin/post/fac1b4e5-c8c5-4d05-9e98-0bb3fb0534e7/bfs.png)
![기초 구현 관련 이미지](https://www.fun-coding.org/00_Images/BFSDFS.png)
