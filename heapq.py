class HeapqEquivalent:
    def __init__(self):
        self.heap = []

    def heappush(self, item):
        self.heap.append(item)
        self._shiftup(len(self.heap) - 1)

    def heappop(self):
        if not self.heap:
            raise IndexError("pop from an empty heap")
        lastelt = self.heap.pop()
        if not self.heap:
            return lastelt
        min_item = self.heap[0]
        self.heap[0] = lastelt
        self._siftdown(0)
        return min_item

    def heapify(self, iterable):
        self.heap = list(iterable)
        for i in reversed(range(len(self.heap) // 2)):
            self._siftdown(i)

    def heappushpop(self, item):
        if self.heap and item > self.heap[0]:
            item, self.heap[0] = self.heap[0], item
            self._siftdown(0)
        return item

    def heapreplace(self, item):
        if not self.heap:
            raise IndexError("replace on empty heap")
        min_item = self.heap[0]
        self.heap[0] = item
        self._siftdown(0)
        return min_item

    def nlargest(self, n):
        return sorted(self.heap, reverse=True)[:n]

    def nsmallest(self, n):
        return sorted(self.heap)[:n]

    def _shiftup(self, pos):
        child = pos
        while child > 0:
            parent = (child - 1) // 2
            if self.heap[child] < self.heap[parent]:
                self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
                child = parent
            else:
                break

    def _siftdown(self, pos):
        end_pos = len(self.heap)
        root = pos
        child = 2 * root + 1
        while child < end_pos:
            right = child + 1
            if right < end_pos and self.heap[right] < self.heap[child]:
                child = right

            if self.heap[child] < self.heap[root]:
                self.heap[child], self.heap[root] = self.heap[root], self.heap[child]
                root = child
                child = 2 * root + 1
            else:
                break


heap = HeapqEquivalent()
heap.heappush(10)
heap.heappush(5)
heap.heappush(3)
heap.heappush(8)

print("힙의 최솟값:", heap.heappop())
heap.heapify([7, 1, 5, 9, 3])
print("힙에서 가장 큰 2개의 요소:", heap.nlargest(2))
print("힙에서 가장 작은 3개의 요소:", heap.nsmallest(3))
print("힙에 6 추가 후 최소 제거:", heap.heappushpop(6))
print("최소를 2개로 교체 후 반환:", heap.heappushpop(2))

print("힙 내용:", heap.heap)
