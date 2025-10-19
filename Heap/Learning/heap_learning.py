class Heap:
    def __init__(self):
        self.arr = []

    def insert(self, val):
        self.arr.append(val)
        n = len(self.arr)
        # Get the last index
        index = n - 1
        while index > 0:
            parent = (index - 1) // 2
            # compare the index with the parent index
            # if parent index value is less than last index then swap
            # new index will be parent
            if self.arr[parent] < self.arr[index]:
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
                index = parent
            else:
                return

    def delete(self):
        if len(self.arr) == 0:
            return print("Nothing to delete")
        # Get last index element
        lastIndex = len(self.arr) - 1
        # put the value of the last index element in first index
        self.arr[0] = self.arr[lastIndex]
        # from index 0 check the both left and right elements in the heap
        # and swap accordingly
        index = 0
        self.arr.pop()
        n = len(self.arr)
        # Place the node in correct position (max-Heap)
        while index < n:
            leftIndex = 2 * index + 1
            rightIndex = 2 * index + 2
            if leftIndex < n and self.arr[index] < self.arr[leftIndex]:
                self.arr[leftIndex], self.arr[index] = (
                    self.arr[index],
                    self.arr[leftIndex],
                )
                index = leftIndex
            elif leftIndex < n and self.arr[index] < self.arr[rightIndex]:
                self.arr[rightIndex], self.arr[index] = (
                    self.arr[index],
                    self.arr[rightIndex],
                )
                index = rightIndex
            else:
                return

    def heapify(self, arr):
        n = len(arr)
        # A leaf node is defined as a node that has no children and which themselves are heap
        # leaf node begin from floor(n/2) to n - 1 index
        # Since we have to heapify the remaining node in the length "n" array
        # So we will iterate from floor(n - 1)/2 till 0th index
        # 0----------n/2--------n-1  total = n
        # previous node before n/2 is (n - 1)/ 2
        for i in range((n - 1) // 2, -1, -1):
            self.transformIntoHeap(arr, n, i)

    def transformIntoHeap(self, arr, n, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < n and arr[largest] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != index:
            arr[largest], arr[index] = arr[index], arr[largest]
            self.transformIntoHeap(arr, n, largest)

    def heapSort(self, arr):
        if len(self.arr) == 0:
            print("array is empty")
        n = len(arr)
        # Step 1 : Build Heap
        self.heapify(arr)
        # Iterate in backward direction
        # range(n - 1, 0, -1) is correct because:
        # You stop just before index 0, which is the last remaining item and already in place.
        # It avoids redundant work and is optimal

        # range(n - 1, -1, -1)  is incorrect
        # You’d do an extra unnecessary swap when i == 0.
        # Heapifying a 1-element array is pointless and can be inefficient
        # or lead to index errors if not handled carefully.
        for i in range(n - 1, 0, -1):
            # Step 2 : Swap first and last index elements
            arr[0], arr[i] = arr[i], arr[0]
            self.transformIntoHeap(arr, i, 0)

    def printHeap(self):
        print(self.arr)


answer = Heap()
answer.insert(50)
answer.insert(54)
answer.insert(53)
answer.insert(52)
answer.insert(55)
answer.insert(70)
answer.printHeap()
answer.delete()
answer.printHeap()
print("===========Heapify===========")
arr = [64, 65, 63, 62, 60]
answer.heapify(arr)
print(arr)
print("===========Heap Sort===========")
arr2 = [12, 11, 13, 5, 6, 7]
answer.heapSort(arr2)
print(arr2)
