class EmptyHeapException(Exception):
    pass


class Heap:
    def __init__(self):
        self.heap = []

    # Create heap from list
    def createHeap(self, list1):
        for value in list1:
            self.insert(value)

    # Insert element into heap (Max Heap)
    def insert(self, value):
        self.heap.append(value)   # Add at end
        index = len(self.heap) - 1

        # Bubble Up
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[parent] < self.heap[index]:
                # Swap
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    # Return top element
    def top(self):
        if not self.heap:
            raise EmptyHeapException()
        return self.heap[0]

    # Delete max element
    def delete(self):
        if not self.heap:
            raise EmptyHeapException()

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]

        # Move last element to root
        last_value = self.heap.pop()
        self.heap[0] = last_value

        index = 0

        # Bubble Down
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left

            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

        return max_value

    # Heap Sort
    def heapSort(self, list1):
        self.heap = []
        self.createHeap(list1)

        sorted_list = []

        while self.heap:
            sorted_list.append(self.delete())

        return sorted_list


# Test
list1 = [23, 6, 3, 77, 45, 79, 43, 2, 55, 345, 33]

h = Heap()
sorted_result = h.heapSort(list1)

print("Sorted List (Descending):", sorted_result)