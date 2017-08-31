__author__ = 'yghou'
"""

"""


class MaxHeap:
    def __init__(self, array=None):
        if array:
            self.heap = self._max_heapify(array)
        else:
            self.heap = []
        pass

    def _sink(self, array, i):

        length = len(array)

        left = 2 * i + 1
        right = 2 * i + 2
        max_index = i

        if left < length and array[max_index] < array[left]:
            max_index = left
        if right < length and array[max_index] < array[right]:
            max_index = right

        if max_index != i:
            array[max_index], array[i] = array[i], array[max_index]
            self._sink(array, max_index)

    def _swim(self, array, i):
        if i == 0:
            return

        parent = (i - 1) / 2
        max_index = i
        if array[i] > array[parent]:
            array[i], array[max_index] = array[max_index], array[i]
            self._swim(array, parent)

    def _max_heapify(self, array):
        for i in xrange(len(array) / 2, -1, -1):
            self._sink(array, i)

        return array

    def pop(self):

        if len(self.heap) == 0:
            return None

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        result = self.heap.pop()
        self._sink(self.heap, 0)
        return result

    def push(self, item):
        self.heap.append(item)
        self._swim(self.heap, len(self.heap) - 1)


if __name__ == '__main__':
    arr = [3, 4, 5, 1, 2, 3, 9, 10, 0, 222]
    heap = MaxHeap(arr)
    length = len(heap.heap)
    for i in xrange(length):
        print heap.pop()