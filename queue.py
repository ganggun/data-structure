class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("큐 크기:", queue.size())
print("큐에서 꺼낸 요소:", queue.dequeue())
print("큐 크기:", queue.size())
print("큐가 비어 있는가:", queue.is_empty())
