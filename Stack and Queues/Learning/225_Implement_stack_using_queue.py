class MyStack:

    def __init__(self):
        self.end = -1
        self.size = 0
        self.arr = []

    def push(self, x):
        if self.size == 0:
            self.end += 1
        else:
            self.end += 1
        self.size += 1
        self.arr.append(x)

    def pop(self):
        if self.size > 0:
            pop_elem = self.arr.pop()
            self.size -= 1
            self.end -= 1
            return pop_elem

    def top(self):
        if self.size > 0:
            return self.arr[self.end]
        return -1

    def empty(self):
        if self.size == 0:
            return True
        return False
