import sys
from collections import deque

MINIMUM_HEIGHT = 0
input = sys.stdin.readline
# //-- debug functions--//


def print_map(map_list):
    print("print_map_result")
    for M in map_list:
        for N in M:
            print(N, "", end="")
        print()


# //-- setup functions --//


def setup_input() -> (int, int, list):
    N = int(input())
    map_list = []
    max_height = MINIMUM_HEIGHT
    for _ in range(N):
        row = list(map(int, input().split()))
        map_list.append(row)
        row_max = max(row)
        max_height = max(row_max, max_height)

    return N, max_height, map_list


# //-- solution functions --//


def solve(N, max_height, map_list):
    max_safe_zone = 0
    for height in range(0, max_height + 2):
        safe_zone = search_safe_zone(N, height, map_list)
        max_safe_zone = max(safe_zone, max_safe_zone)

    print(max_safe_zone)


def search_safe_zone(N, height, map_list):
    safe_zone = 0
    visit_map = [[1] * N for _ in range(N)]
    for xpos in range(N):
        for ypos in range(N):
            start_pos = [xpos, ypos]
            to_visit = deque()
            to_visit.append(start_pos)
            if map_list[xpos][ypos] > height and visit_map[xpos][ypos] == 1:
                search_map(to_visit, visit_map, map_list, height, N)
                safe_zone += 1
    # print("height: ", height, "finished : ", safe_zone)
    return safe_zone


def search_map(to_visit, visit_map, map_list, height, N):
    while to_visit:
        #debug_visit_map(visit_map, to_visit)
        xpos, ypos = to_visit.popleft()
        visit_map[xpos][ypos] = 0
        search_visitable(xpos, ypos, N, visit_map, to_visit, map_list, height)


def search_visitable(xpos, ypos, N, visit_map, to_visit, map_list, height):
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for dx, dy in direction:
        next_x = xpos + dx
        next_y = ypos + dy
        if (
            0 <= next_x < N
            and 0 <= next_y < N
            and visit_map[next_x][next_y] == 1
            and [next_x, next_y] not in to_visit
            and map_list[next_x][next_y] > height
        ):
            to_visit.append([next_x, next_y])


def debug_visit_map(visit_map, to_visit):
    print("to_visit :", to_visit)
    print_map(visit_map)
    input()


# //-- main code --//


if __name__ == "__main__":
    N, max_height, map_list = setup_input()
    solve(N, max_height, map_list)
