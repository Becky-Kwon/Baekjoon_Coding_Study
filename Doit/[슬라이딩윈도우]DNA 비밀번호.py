# 12891 - DNA 비밀번호
checklist = [0]*4
mylist = [0]*4
checkSecret = 0

# 추가 함수
def myadd(c):
    global checklist, checkSecret, mylist
    if c == 'A':
        mylist[0] += 1
        if mylist[0] == checklist[0]:
            checkSecret += 1
    elif c == 'C':
        mylist[1] += 1
        if mylist[1] == checklist[1]:
            checkSecret += 1
    elif c == 'G':
        mylist[2] += 1
        if mylist[2] == checklist[2]:
            checkSecret += 1
    elif c == 'T':
        mylist[3] += 1
        if mylist[3] == checklist[3]:
            checkSecret += 1

# 삭제 함수
def myremove(c):
    global checklist, checkSecret, mylist
    if c == 'A':
        if mylist[0] == checklist[0]:
            checkSecret -= 1
        mylist[0] -= 1
    elif c == 'C':
        if mylist[1] == checklist[1]:
            checkSecret -= 1
        mylist[1] -= 1
    elif c == 'G':
        if mylist[2] == checklist[2]:
            checkSecret -= 1
        mylist[2] -= 1
    elif c == 'T':
        if mylist[3] == checklist[3]:
            checkSecret -= 1
        mylist[3] -= 1

# 메인
T, P = map(int, input().split())
A = input()
checklist = list(map(int, input().split()))
# 만들 수 있는 종류 개수
result = 0
# 예시
# T = 9
# P = 8
# A = 'CCTGGATTG'
# checklist = [2,0,1,1]

for i in range(4):
    if checklist[i] == 0:
        checkSecret += 1

# 맨 처음 window 판단
for i in range(P):
    myadd(A[i])
if checkSecret == 4:
    result += 1
#print(mylist)

# window 움직이면서 판단
for j in range(P, T):
    i = j - P
    myadd(A[j])
    myremove(A[i])
    #print('mylist:', mylist)
    #print('check:', checkSecret)
    if checkSecret == 4:
        result += 1

print(result)






