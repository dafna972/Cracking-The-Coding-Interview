from Node import Node
from Stack import Stack

def Palindrome(head):
    stack = Stack()
    pointer1 = head
    pointer2 = head.next
    while pointer2 != None and pointer2.next != None:
        stack.push(pointer1)
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next

    if pointer2 == None:
        pointer1 = pointer1.next
    else: 
        stack.push(pointer1)
        pointer1 = pointer1.next

    while pointer1 != None and stack.pop().data == pointer1.data:
        pointer1 = pointer1.next

    if pointer1 == None:
        return True
    return False

n1 = Node(data = 7)
n2 = Node(data = 2)
n3 = Node(data = 6)
n4 = Node(data = 6)
n5 = Node(data = 2)
n6 = Node(data = 7)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
print(Palindrome(n1))