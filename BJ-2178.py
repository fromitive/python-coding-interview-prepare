"""
DFS는 선택한 길이 최적의 길이 아닐경우에 최단 경로를 보장하지 않지만 BFS는 인접한 방문가능한 노드들부터 차근차근 살펴보기 때문에 최단 거리를 구할 수 있게 되어 BFS가 좋다.

Graph Search 알고리즘의 특성 - 연결가능한 모든 점들을 다 살펴본다. 다만 깊이우선적으로 탐색할 것인지 너비 우선적으로 탐색할 것 인지에 따라 다르다

DFS
DFS는 Stack 으로 구현할 수 있다. 맨 우선적으로 넣은 경로가 결국 나중에 탐색이 된다(LIFO)

BFS
BFS는 Queue 로 구현할 수 있다. 노드 경로를 추가할때 맨 우선적으로 넣은 경로가 먼저 탐색이 된다 (FIFO)


DFS는 python으로 아래와 같이 구성된다.

while stack:
    node = stack.pop()
    search_next_node(node, stack)


BFS는 python으로 아래와 같이 구성된다.

from collections import deque

while queue:
    node = queue.popleft()
    search_next_node(node, queue)

General 하게 짜려면 다음과같은 구성이다

while to_visit
    node = to_visit.get_node()
    search_next_node(node, to_visit)
"""

from collections import deque


def setup_input() -> (int, int, list):
    N, M = map(int, input().split())
    map_list = []
    for _ in range(N):
        map_list.append([int(m) for m in input()])

    return N, M, map_list


def print_map(map_list):
    for M in map_list:
        for N in M:
            print(N, "", end="")
        print()


def debug_print(to_visit, map_list):
    print("to_visit :", to_visit)
    print("map_list :")
    print_map(map_list)
    input()


def solve(N, M, map_list):
    to_visit = deque()  # 미로의 최단 경로를 찾기 위해 deque 사용
    to_visit.append([0, 0])
    while to_visit:
        x, y = to_visit.popleft()
        append_next_step(to_visit, x, y, N, M, map_list)
        debug_print(to_visit, map_list)


def append_next_step(to_visit, x, y, N, M, map_list):
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for dx, dy in directions:
        next_x = x + dx
        next_y = y + dy
        if 0 <= next_x < N and 0 <= next_y < M and map_list[next_x][next_y] == 1:
            to_visit.append([next_x, next_y])
            map_list[next_x][next_y] = map_list[x][y] + 1


N, M, map_list = setup_input()
solve(N, M, map_list)
