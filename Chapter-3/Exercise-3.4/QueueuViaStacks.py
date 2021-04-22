def push(item):
    stack1.push(stack2.pop())
    stack2.push(item)
    stack2.push(stack1.pop())

def pop():
    stack2.pop()