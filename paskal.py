def solve(number_of_rows: int):
    result = [[1]]
    for i in range(number_of_rows - 1):
        next_value = [0] + result[-1] + [0]
        next_angle = []
        for j in range(len(result[-1]) + 1):
            next_angle.append(next_value[j] + next_value[j + 1])
        result.append(next_angle)
    return result


def print_result(result):
    print("result is :")
    for row in result:
        print(row)


number_of_rows = int(input())

result = solve(number_of_rows)

print_result(result)
