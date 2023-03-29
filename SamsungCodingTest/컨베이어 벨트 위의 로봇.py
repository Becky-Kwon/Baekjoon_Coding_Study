# 20055 - 컨베이어 벨트 위의 로봇
# 삼성 코테 기출

# 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
# 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
#    - 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

# 전역변수 생성

#N, K = map(int, input().split())
#belt = list(map(int, input().split()))

N = 3  #N
K = 2  #K
belt = [1, 2, 1, 2, 1, 2]
belt.insert(0, -100)   # belt 맨 앞에 -100 추가해서 1~2N개가 인덱스 명 자체로 쓰이게 함
robots = [] # 로봇들의 위치를 나타내는 리스트
is_robot = [False for _ in range(len(belt))] # 해당 컨베이어 벨트의 index에 로봇이 있는지 없는지를 알려주는 리스트

# [1] 벨트 및 로봇 회전
def belt_rotate():
    global belt, robots, is_robot
    # 벨트 회전
    a_2N = belt.pop()
    belt.insert(1, a_2N)
    # 로봇 회전
    new_robots = []
    is_robot = [False for _ in range(len(belt))]
    for robot_index in robots:
        next_robot_index = robot_index + 1
        # 다음칸이 N이 아니라면 이동
        if next_robot_index < N:
            new_robots.append(robot_index+1)
            is_robot[robot_index+1] = True
        robots = new_robots

# [2] 로봇 이동 : 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
# 만약 이동할 수 없다면 가만히 있는다. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며,
# 그 칸의 내구도가 1 이상 남아 있어야 한다.
def robot_move():
    global belt, robots, is_robot
    new_robots = []  # 새로운 로봇 배열
    for robot_index in robots:
        next_robot_index = robot_index + 1 # 다음 로봇의 위치
        # 이동이 불가능한 경우(로봇이 있거나 내구도 1미만)
        if is_robot[next_robot_index] or belt[next_robot_index] < 1:
            new_robots.append(robot_index)
        else:  # 이동이 가능한 경우
            belt[next_robot_index] -= 1  # 다음 위치의 벨트 내구도 1 감소
            is_robot[robot_index] = False  # 현재 위치에 로봇이 존재하지 않게됨
            if next_robot_index != N:  # 다음 위치가 N이 아닌경우에만(중요)
                new_robots.append(next_robot_index)  # 새로운 로봇 배열에 추가
                is_robot[next_robot_index] = True
    robots = new_robots

# [3] 로봇 삽입
# 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
def robot_insert():
    global belt, robots, is_robot
    if belt[1] != 0:
        robots.append(1)
        is_robot[1] = True
        belt[1] -=1

# [4] 종료 조건 확인
# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
def check():
    global belt, robots, is_robot, K
    count_ = belt.count(0)
    return count_ >= K


cnt = 0
while not check():  # check() 함수가 True를 반환할 때 까지 반복
    cnt += 1
    # 1. 컨베이어 및 로봇 회전
    belt_rotate()
    # 2. 로봇 이동
    robot_move()
    # 3. 로봇 삽입
    robot_insert()

print(cnt)









