# 다음 순열의 값은 이전 순열의 값으로 형성되어야 함
# next_value -> 0 + (이전 배열) + 0

# 반복문의 끝은 이전 배열의 길이에 의존됨
# for j in range(len(result[-1] + 1)) # 이전 배열의 길이 + 1까지 반복

def solve(number_of_rows: int):
    result = [[1]]
    for i in range(number_of_rows - 1):
        next_value = [0] + result[-1] + [0]
        next_line = []
        for j in range(len(result[-1]) + 1):
            next_line.append(next_value[j] + next_value[j + 1])
        result.append(next_line)
    return result


def print_result(result):
    print("result is :")
    for row in result:
        print(row)


number_of_rows = int(input())

result = solve(number_of_rows)

print_result(result)
