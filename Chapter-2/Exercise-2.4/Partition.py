import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Node import Node

def Partition(head, partition_node):
    smaller = Node()
    larger = Node()
    smaller_head = None
    larger_head = None
    while head != None:
        if head.data < partition_node.data:
            smaller.next = Node(data=head.data)
            if smaller_head == None:
                smaller_head = smaller
            smaller = smaller.next
        else:
            larger.next = Node(data=head.data)
            if larger_head == None:
                larger_head = larger
            larger = larger.next
        head = head.next
    
    smaller.next = larger_head

    return smaller_head

n1 = Node(data=1.0)
n2 = Node(data=2.5)
n3 = Node(data=3.0)
n5 = Node(data=2.0)
n4 = Node(data=0.0)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(n1)
n1 = Partition(n1,n2)
print(n1)