class Solution:
    def asteroidCollisionStriver(self, asteroids):
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop()
                if stack and stack[-1] == abs(asteroids[i]):
                    stack.pop()
                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroids[i])
        return stack

    def asteroidCollision(self, asteroids):
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                # If diff is -ve then pop the element from the stack
                if diff < 0:
                    stack.pop()
                # If diff is positive then move to the next iterator by assigning a = 0
                # so that the while loop breaks
                elif diff > 0:
                    a = 0
                # If diff is equal to zero it means that the stack top element is equal to the current element
                # then assign a = 0 so that the while loop breaks and pop the element in the stack
                else:
                    a = 0
                    stack.pop()
            # Append a if it is not zero
            if a:
                stack.append(a)
        return stack


answer = Solution()
asteroids = [-2, 5, 10, -5]
print(answer.asteroidCollisionStriver(asteroids))
print(answer.asteroidCollision(asteroids))
