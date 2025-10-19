class Solution:
    def totalFruitsBrute(self, fruits):
        total = 0
        for i in range(len(fruits)):
            typeSet = set()
            for j in range(i, len(fruits)):
                typeSet.add(fruits[j])
                if len(typeSet) <= 2:
                    total = max(total, j - i + 1)
                else:
                    break
        return total

    # TC = O(2n)
    # SC = O(3)
    def totalFruitsBetter(self, fruits):
        l = 0
        r = 0
        total = 0
        fruits_map = {}
        while r < len(fruits):
            fruits_map[fruits[r]] = 1 + fruits_map.get(fruits[r], 0)
            if len(fruits_map) > 2:
                # At worst case O(n)
                while len(fruits_map) > 2:
                    fruits_map[fruits[l]] -= 1
                    if fruits_map[fruits[l]] == 0:
                        del fruits_map[fruits[l]]
                    l += 1
            if len(fruits_map) <= 2:
                total = max(total, r - l + 1)
            r += 1
        return total

    def totalFruitsOptimal(self, fruits):
        l = 0
        r = 0
        total = 0
        fruits_map = {}
        while r < len(fruits):
            fruits_map[fruits[r]] = 1 + fruits_map.get(fruits[r], 0)
            if len(fruits_map) > 2:
                fruits_map[fruits[l]] -= 1
                if fruits_map[fruits[l]] == 0:
                    del fruits_map[fruits[l]]
                l += 1
            if len(fruits_map) <= 2:
                total = max(total, r - l + 1)
            r += 1
        return total


answer = Solution()
fruits = [1, 2, 1]
print(answer.totalFruitsBrute(fruits))
print(answer.totalFruitsBetter(fruits))
print(answer.totalFruitsOptimal(fruits))
