import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Node import Node

def DeleteMiddleNode(node):
    node.data = node.next.data
    temp = node.next
    node.next = node.next.next
    temp = None
    

n1 = Node(data=1)
n2 = Node(data=2)
n3 = Node(data=3)
n1.next = n2
n2.next = n3
print(n1)
DeleteMiddleNode(n2)
print(n1)