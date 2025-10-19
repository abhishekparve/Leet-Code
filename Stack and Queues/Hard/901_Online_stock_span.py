class Solution:  # Brute Force
    # TC = O(n^2) = O(number of days)
    # Sc = O(n)
    def __init__(self):
        self.prices = []

    def next(self, price):
        self.prices.append(price)
        span = 1
        for i in range(len(self.prices) - 2, -1, -1):
            if self.prices[i] <= price:
                span += 1
            else:
                break
        return span


class StockSpanner:
    # TC = O(n)
    # SC = O(n)
    def __init__(self):
        self.stack = []  # (price, span) ==> indexes (0, 1)

    def next(self, price):
        span = 1
        # stack[-1][0] means getting the top element of the stack and at index 0 we have price
        # so we compare stack top element price with the input price
        while self.stack and self.stack[-1][0] <= price:
            # pop the top element of stack but getting the value(span) at 1st index of the
            # popped elemnet and adding it to the answer
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


answer = StockSpanner()
print(answer.next(100))
print(answer.next(80))
print(answer.next(60))
print(answer.next(70))
print(answer.next(60))
print(answer.next(75))
print(answer.next(80))
