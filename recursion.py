from typing import List


def total(items: List):
    result = 0
    for item in items:
        if isinstance(item,int):
            result += item
        else:
            result += total(item)
            
    return result


items = [ 1, 2, 3, [4, 5], 6, 7, [8,[9,10]]]

print(total(items)) # 55
