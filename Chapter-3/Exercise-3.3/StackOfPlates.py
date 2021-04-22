stacks_array = [[]]
stack_index = -1
internal_index = -1
maximum_stack_size = 8

def pop():
    global internal_index, stack_index, maximum_stack_size
    if internal_index >= 0:
        result = stacks_array[stack_index][internal_index]
        internal_index -= 1
        return result
    
    if stack_index >= 0:
        internal_index = maximum_stack_size - 1
        stack_index -= 1
        result = stacks_array[stack_index][internal_index]
        return result

def push(item):
    global internal_index, stack_index, maximum_stack_size
    if internal_index < maximum_stack_size:
        stacks_array[stack_index].append(item)
        internal_index += 1
        return
    
    stacks_array.append([item])
    stack_index += 1
    internal_index = 0

push(9)
push(8)
push(7)
a = pop()
push(6)
pop()
pop()
pop()

