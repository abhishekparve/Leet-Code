class Solution:
    # TC = O(n)
    # SC = O(1)
    def lemonadeChange(self, bills):
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                # return $5 to the customer and get $10
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif bill == 20:
                # to return change of 15 you can give 10 and 5 or three 5 dollars
                if ten > 0 and five > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


answer = Solution()
bills = [5, 5, 10, 10, 20]
print(answer.lemonadeChange(bills))
