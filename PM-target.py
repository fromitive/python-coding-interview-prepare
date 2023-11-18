class Problem:
    def __init__(self):
        self.target = int(input())
        self.operands = list(map(int, input().split()))
        self.answer = 0

    def solution(self):
        stack = []
        stack.append([self.operands[0], 0])
        stack.append([-self.operands[0], 0])
        while stack:
            result, idx = stack.pop()
            self.search_next(result, idx, stack)
            print("stack :", stack, "answers : ", self.answer)
            input()
        return self.answer

    def search_next(self, result, idx, stack):
        next_idx = idx + 1
        if next_idx != len(self.operands):
            next_idx = idx + 1
            stack.append([result + self.operands[next_idx], next_idx])
            stack.append([result - self.operands[next_idx], next_idx])
        if next_idx == len(self.operands):
            if result == self.target:
                self.answer += 1


problem = Problem()
problem.solution()
