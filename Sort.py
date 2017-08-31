__author__ = 'yghou'


class Sort:
    def merge_sort(self, arr):

        if len(arr) <= 1:
            return arr

        mid = len(arr) / 2

        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self._merge_sorted_array(left, right)

    def _merge_sorted_array(self, A, B):
        sorted_array = []
        l = 0
        r = 0

        while l < len(A) and r < len(B):
            if A[l] < B[r]:
                sorted_array.append(A[l])
                l += 1
            else:
                sorted_array.append(B[r])
                r += 1

        sorted_array += A[l:]
        sorted_array += B[r:]
        return sorted_array


    def qsort(self, array):

        if not array:
            return []
        else:
            pivot = array[0]
            less = [x for x in array if x < pivot]
            more = [x for x in array[1:] if x >= pivot]
            return self.qsort(less) + [pivot] + self.qsort(more)


if __name__ == '__main__':
    sort = Sort()
    arr = [2, 3, 4, 1, 11, 44, 52, 1123, 99]
    print sort.merge_sort(arr)
    print sort.qsort(arr)