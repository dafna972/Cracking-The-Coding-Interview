from Queue import Queue 

stack = []
linked_lists = []
headers = []
depth = 0
current = None

"""
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done."""

def ListOfDepths(node):
    
    AddToList(node, depth)
    depth += 1


def AddToList(node, depth):
    if len(linked_lists) < depth:
        linked_lists.append(node)
        headers.append(node)
    else:
        linked_lists[i].next = node
        temp = linked_lists[i]
        linked_lists[i] = node

current = root
while current != None and not stack.is_empty():
    