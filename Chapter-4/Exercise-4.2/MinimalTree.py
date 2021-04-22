from Node import Node

def MinimalTree(nodes, size):
    if nodes == []:
        return None
    root_index = 0
    add = False
    if size % 2 == 0:
        root_index = int(size / 2) - 1
    else:
        add = True
        root_index = int((size + 1) / 2) - 1

    root = Node(data = nodes[root_index])
    if root_index == 0:
        return root
    root.left_child = MinimalTree(nodes[0:root_index], root_index)
    if add:
        root.right_child = MinimalTree(nodes[root_index + 1: size], root_index + 1)
    else:
         root.right_child = MinimalTree(nodes[root_index + 1: size], root_index)

    return root  

print(MinimalTree([0,1,2,3,4,5,6],7))     