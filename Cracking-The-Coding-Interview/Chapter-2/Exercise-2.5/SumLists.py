import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Node import Node

def SumLists(number1, number2):
    result_head = None
    result = Node()
    add_one = False
    while number1 != None:
        current_sum = number1.data+number2.data
        if current_sum < 10:            
            result.next = Node(data=current_sum)
            if add_one:
                result.next.data += 1
            add_one = False
        else:
            result.next = Node(data=current_sum%10)
            if add_one:
                result.next.data += 1
            add_one = True
        if result_head == None:
            result_head = result
        number1 = number1.next
        number2=number2.next
        result = result.next
    return result_head.next

n1 = Node(data = 7)
n2 = Node(data = 1)
n3 = Node(data = 6)
n4 = Node(data = 5)
n5 = Node(data = 9)
n6 = Node(data = 2)
n1.next=n2
n2.next=n3
n4.next=n5
n5.next=n6
print(SumLists(n1,n4))