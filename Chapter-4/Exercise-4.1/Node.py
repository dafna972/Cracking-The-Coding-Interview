class Node:
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children
        self.visited = False