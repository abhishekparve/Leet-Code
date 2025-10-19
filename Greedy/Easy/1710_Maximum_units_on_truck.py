from operator import itemgetter


class Solution:
    # Same as fractional KnapSnack GFG
    # but here you already have unitsPerBoxes
    # so you have to sort based on the maximum values of unitsPerBoxes which makes it easier
    # in reverse order. Logic wise every thing is same
    # TC = O(nlogn + n)
    # SC = O(1)
    def maxUnits(self, boxTypes, truckSize):
        # Sorting using itemgetter based on UnitsPerBoxes
        # boxTypes.sort(key=itemgetter(1), reverse=True)
        # Sorting using lambda
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        totalUnits = 0
        for box, uintsPerBox in boxTypes:
            if box <= truckSize:
                totalUnits += box * uintsPerBox
                truckSize -= box
            else:
                totalUnits += uintsPerBox * truckSize
                break
        return totalUnits


answer = Solution()
boxTypes = [[1, 3], [2, 2], [3, 1]]
truckSize = 4
print(answer.maxUnits(boxTypes, truckSize))
