# https://leetcode.com/problems/maximum-frequency-stack/description/


# TC = O(1) and SC = O(2n)
class FreqStack:
    def __init__(self):
        self.elem_freq_count = {}
        self.groups = {}
        self.max_count = 0

    def push(self, val):
        valCount = self.elem_freq_count.get(val, 0) + 1
        self.elem_freq_count[val] = valCount
        if valCount > self.max_count:
            self.max_count = valCount
            self.groups[valCount] = []
        self.groups[valCount].append(val)

    def pop(self):
        # val should alwayes be popped from groups dictionary
        val = self.groups[self.max_count].pop()
        self.elem_freq_count[val] -= 1
        if not self.groups[self.max_count]:
            self.max_count -= 1
        return val


answer = FreqStack()
answer.push(5)
answer.push(7)
answer.push(5)
answer.push(7)
answer.push(4)
answer.push(5)
print(answer.pop())
print(answer.pop())
print(answer.pop())
print(answer.pop())
