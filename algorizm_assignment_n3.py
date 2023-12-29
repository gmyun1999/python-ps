"""
원리:
(a,b)점에 위치해있을때 y = x-a+b , y = -x+a+b 두개의 직선을 만들어내기에 나머지 점들이 이 위치에 있으면 안됨
한 row 에서 위치할수있는 체스말은 어짜피 한개이므로 row 를 1부터 n까지 순환하면서 col 과 대각선만 신경써주면됨
모든 해를 구해야하므로 트리 전체를 dfs 로 순회해야하지만 가능성이 없는 부분은 pruning을 통해서 연산을 줄인다.

적용한 pruning:
1. solution을 발견하고 backtracking 하는 과정에서 맨 마지막에 한 2개를 동시에 없앰
2. 한 row 에서 연산이 불가능 하면 그밑에는 연산 필요 x

코드설명:
queen_location -> index 순서가 row 의 순서이다. element value 값이 col이다.
row 를 순환하면서 해당 col 에 퀸을 배치할수있으면 일단 배치시키고 넘어간다.
더이상 배치가 불가능한 row 가 있으면 바로 전 row 의 queen_location의 원소값을 삭제시키고 삭제한 원소의 col +1 부터 서치한다
col 이 n보다 커졌을경우 배치할수 없는것으로 판단하여 백트래킹한다.
참고:
문제에서 n이 3이상이라고 해서 n=1일때 고려하지않았다.
코드가 최적화 및 다듬지 않아서 가독성이 구립니다 ㅠ
"""


def show_first_solution(lst):
    for i in range(len(lst)):
        buff = ['-'] * len(lst)
        buff[lst[i] - 1] = 'Q'
        print(''.join(buff))


n = int(input())
queen_location = []
i = 1
j = 1
cnt = 0
while 0 < i < n + 1:
    can_locate = True
    while j < n + 1:
        can_locate = True
        for idx in range(len(queen_location)):
            row = idx + 1
            if queen_location[idx] == j:
                can_locate = False
                break
            elif queen_location[idx] + row == i + j or queen_location[idx] - row == j - i:
                can_locate = False
                break
            else:
                continue

        if can_locate:
            queen_location.append(j)
            break
        else:
            j += 1
    if j == n + 1:
        can_locate = False
    if len(queen_location) == n:
        cnt += 1
        if cnt == 1:
            show_first_solution(queen_location)
        queen_location.pop()
        i -= 1
        j = 1 + queen_location.pop()
    else:
        if can_locate:
            i += 1
            j = 1
        else:
            i -= 1
            if i != 0:
                j = queen_location.pop() + 1
            else:
                break
print(cnt)
