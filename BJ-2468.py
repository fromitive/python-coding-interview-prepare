MINIMUM_HEIGHT = 1

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
    for height in range(1, max_height + 1):
        visit_map = make_visit_map(N, height, map_list)
        safe_zone = search_safe_zone(N, visit_map)
        max_safe_zone = max(safe_zone, max_safe_zone)

    print(max_safe_zone)


def make_visit_map(N, height, map_list):
    # 1 can visit
    # 0 can't visit
    visit_map = [[1] * N for _ in range(N)]
    for xpos in range(N):
        for ypos in range(N):
            if map_list[xpos][ypos] <= height:
                visit_map[xpos][ypos] = 0
    return visit_map


def search_safe_zone(N, visit_map):
    safe_zone = 0

    for xpos in range(N):
        for ypos in range(N):
            start_pos = [xpos, ypos]
            to_visit = [start_pos]
            if visit_map[xpos][ypos] == 1:
                search_map(to_visit, visit_map)
                safe_zone += 1
    print("finished : ", safe_zone)
    return safe_zone


def search_map(to_visit, visit_map):
    while to_visit:
        debug_visit_map(visit_map, to_visit)
        xpos, ypos = to_visit.pop()
        visit_map[xpos][ypos] = 0
        search_visitable(xpos, ypos, N, visit_map, to_visit)


def search_visitable(xpos, ypos, N, visit_map, to_visit):
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for dx, dy in direction:
        next_x = xpos + dx
        next_y = ypos + dy
        if (
            0 <= next_x < N
            and 0 <= next_y < N
            and visit_map[next_x][next_y] == 1
            and [next_x, next_y] not in to_visit
        ):
            to_visit.append([next_x, next_y])


def debug_visit_map(visit_map, to_visit):
    print("to_visit :", to_visit)
    print_map(visit_map)
    input()


# //-- main code --//


if __name__ == "__main__":
    N, max_height, map_list = setup_input()

    print_map(map_list)

    solve(N, max_height, map_list)
