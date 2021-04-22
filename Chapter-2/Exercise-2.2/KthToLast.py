import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Node import Node

def KthToLast(linked_list, kth):
    if kth == 1 and linked_list.next == None:
        return linked_list.data, 1
    if linked_list.next == None:
        return None, 1
    next = KthToLast(linked_list.next, kth)
    if next[0] != None:
        return next
    if next[1] + 1 == kth:
        return linked_list.data, kth
    return None, next[1] + 1

linked_list = Node(Node(Node(Node(),7),6),8)
print(KthToLast(linked_list,2))
print(KthToLast(linked_list,4))
