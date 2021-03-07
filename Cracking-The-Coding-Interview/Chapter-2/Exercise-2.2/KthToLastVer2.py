import os, sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Node import Node

def KthToLastVer2(linked_list, kth):
    pointer1 = linked_list
    pointer2 = linked_list
    for i in range(kth):
        pointer2 = pointer2.next

    while pointer2.next != None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1.data


linked_list = Node(Node(Node(Node(),7),6),8)
print(KthToLastVer2(linked_list,2))
print(KthToLastVer2(linked_list,3))