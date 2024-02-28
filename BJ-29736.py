
solved = list(map(int, input().split()))
my_friends = list(map(int, input().split()))
a = solved[0]
b = solved[1]
k = my_friends[0]
x = my_friends[1]
max_friends = min(k + x, b)
min_friends = max(k - x, a)

answer = max_friends - min_friends + 1

if min_friends < a or min_friends > b or k + x < a or k - x > b:
    answer = "IMPOSSIBLE" 


print(answer)

