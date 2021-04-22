class Stack():
    def __init__(self):
        self.stack = []
        self.items_amount = 0

    def push(self, item):
        self.stack.append(item)
        self.items_amount += 1

    def pop(self):
        self.items_amount -= 1
        return self.stack.pop()

    def peek(self):
        return self.stack[self.items_amount - 1]
        
