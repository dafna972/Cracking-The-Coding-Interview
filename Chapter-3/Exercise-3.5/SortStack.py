def SortStack(stack):
    temp_stack = []
    
    while not stack.IsEmpty():
        temp_stack.push(stack.pop())
        temp = stack.pop()

        # 1 2 3 or 1 3 2 
        if temp_stack.peek() < temp:
            if temp < stack.peek():
                temp_stack.push(temp)
                temp_stack.push(stack.pop())
                continue
        # 2 3 1 or 3 2 1
        if stack.peek() < temp_stack.peek():

        # 2 1 3 or 3 1 2 
        if temp < temp_stack.peek():
            stack.push(temp_stack.pop())
            temp_stack.push(temp)