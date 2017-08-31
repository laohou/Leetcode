__author__ = 'yghou'

"""

"""

import heapq
import collections


class HuffmanCompression:
    class Trie:
        def __init__(self, val, char=''):
            self.val = val
            self.char = char
            self.coding = ''
            self.left =  self.right = None

        def __cmp__(self, other):
            return self.val - other.val

    def __init__(self, string):
        self.string = string
        counter = collections.Counter(string)
        heap = []
        for char, cnt in counter.items():
            heapq.heappush(heap, HuffmanCompression.Trie(cnt, char))

        while len(heap) != 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            trie = HuffmanCompression.Trie(left.val + right.val)
            trie.left, trie.right = left, right
            heapq.heappush(heap, trie)

        self.root = heap[0]
        self.s2b = {}
        self.bfs_encode(self.root, self.s2b)
        print self.s2b

    def bfs_encode(self, root, s2b):
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node.char:
                s2b[node.char] = node.coding
                continue

            if node.left:
                node.left.coding = node.coding + '0'
                queue.append(node.left)

            if node.right:
                node.right.coding = node.coding + '1'
                queue.append(node.right)


    def compress(self, string):
        bits = ''
        for char in string:
            bits += self.s2b[char]
        return bits

    def uncompress(self, bits):
        string = ''
        node = self.root
        for bit in bits:
            if bit == '0':
                node = node.left
            else:
                node = node.right

            if node.char:
                string += node.char
                node = self.root

        return string

def get_rate(compressed_binary, uncompressed_bits):
    return len(compressed_binary) * 100 / uncompressed_bits

if __name__ == '__main__':
    s = 'everyday is awesome!'
    hc = HuffmanCompression(s)
    uncompressed_bits = len(s)*8
    result = hc.compress(s)
    print 'result:', result
    print 'rate:', get_rate(hc.compress(s), uncompressed_bits)
    print 'origin:', hc.uncompress(result)
