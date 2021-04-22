from Node import Node
from Queue import Queue

def RouteBetweenNodes(first_node, second_node):

    queue = Queue()
    queue.enqueue(first_node)
    
    while not queue.is_empty():
        current = queue.dequeue()
        if current.visited:
            continue
        current.visited = True
        if current.name == second_node.name:
            return True
        
        for child in current.children:  
            if not child.visited: 
                queue.enqueue(child)

    return False

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n0.children = [n1,n4,n5]
n1.children = [n3,n4]
n2.children = [n1]
n3.children = [n2,n4]
n4.children = []
n5.children = []

print(RouteBetweenNodes(n0, n2))
print(RouteBetweenNodes(n4, n0))