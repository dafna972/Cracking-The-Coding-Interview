class Queue:
    def __init__(self):
        self.queue = []
        self.counter = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.counter += 1

    def dequeue(self):
        item = self.queue.pop(0)
        self.counter -= 1
        return item

    def is_empty(self):
        return self.counter == 0