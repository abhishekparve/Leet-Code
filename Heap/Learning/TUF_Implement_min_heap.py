class Solution:

    def initializeHeap(self):
        self.arr = []

    def insert(self, key):
        self.arr.append(key)
        n = len(self.arr)
        index = n - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.arr[parent] > self.arr[index]:
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
                index = parent
            else:
                return

    def heapify(self, arr, n, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < n and arr[smallest] > arr[left]:
            smallest = left
        if right < n and arr[smallest] > arr[right]:
            smallest = right

        if smallest != index:
            arr[smallest], arr[index] = arr[index], arr[smallest]
            self.heapify(arr, n, smallest)

    def changeKey(self, index, new_val):
        self.arr[index] = new_val
        n = len(self.arr)
        for i in range((n - 1) // 2, -1, -1):
            self.heapify(self.arr, n, i)

    # Change Key alternative
    # We're heapifying the entire array, which works but is inefficient.
    #  Better approach:
    # If new_val < old_val: move up using parent check (like insert)
    # If new_val > old_val: call heapify() at that index
    def changeKey2(self, index, new_val):
        old_val = self.arr[index]
        self.arr[index] = new_val
        n = len(self.arr)
        if new_val < old_val:
            while index > 0:
                parent = (index - 1) // 2
                if self.arr[parent] > self.arr[index]:
                    self.arr[parent], self.arr[index] = (
                        self.arr[index],
                        self.arr[parent],
                    )
                    # point index as parent
                    index = parent
                else:
                    break
        else:
            self.heapify(self.arr, n, index)

    def extractMin(self):
        if len(self.arr) == 0:
            return None
        root = self.arr[0]
        last = self.arr.pop()
        if len(self.arr) > 0:
            self.arr[0] = last
            self.heapify(self.arr, len(self.arr), 0)
        return root

    def isEmpty(self):
        return len(self.arr) == 0

    def getMin(self):
        if len(self.arr) != 0:
            return self.arr[0]
        return None

    def heapSize(self):
        if len(self.arr) != 0:
            n = len(self.arr)
            return n
        return None
