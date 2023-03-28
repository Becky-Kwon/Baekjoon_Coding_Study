from collections import deque

N, L = map(int, input().split())
mydeque = deque()  #빈 데크 만들기
now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))
    print(mydeque)
    if mydeque[0][1] <= i - L:
        mydeque.popleft()
    print(mydeque[0][0], end = ' ')
