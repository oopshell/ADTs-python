from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None  # Return None if the queue is empty

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 20
