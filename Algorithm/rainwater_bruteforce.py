# 백준  14719 - 빗물
# BruteForce를 활용한 예제

h, w = map(int, input().split())
world = list(map(int, input().split()))
# h = 4
# w = 4
# world = [3, 0, 1, 4]

area = 0

for i in range(1, w-1):
    max_left = max(world[:i])
    max_right = max(world[i+1:])

    if world[i] < max_left and world[i] < max_right:
        if max_left < max_right:
            area += max_left - world[i]
        else : area += max_right - world[i]

print(area)

