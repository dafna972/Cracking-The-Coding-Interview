import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Node import Node

def DeleteMiddleNode(linked_list, node):
    while linked_list.next.data != node:
        linked_list = linked_list.next
    linked_list.next = linked_list.next.next

linked_list = Node(Node(Node(Node(),7),6),8)
print(DeleteMiddleNode(linked_list,6))
print(linked_list)