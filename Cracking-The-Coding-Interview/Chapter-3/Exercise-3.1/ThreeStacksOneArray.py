array = []
pointer1 = 0
pointer2 = 1
pointer3 = 2

def pop1():
    global pointer1
    if pointer1 == 0:
        return
    pop = array[pointer1-3]
    array[pointer1-3] = None
    pointer1 = pointer1 - 3
    return pop


def pop2():
    if pointer2 == 1:
        return
    pop = array[pointer2]
    array[pointer2] = None
    pointer2 -= 3
    return pop


def pop3():
    if pointer3 == 2:
        return
    pop = array[pointer3]
    array[pointer3] = None
    pointer3 -= 3
    return pop

def push1(item):
    global pointer1
    while len(array) - 1 < pointer1:
        array.append(None)
    array[pointer1] = item
    pointer1 = pointer1 + 3


push1(9)
push1(8)
push1(7)
a = pop1()
push1(6)
pop1()
pop1()
pop1()