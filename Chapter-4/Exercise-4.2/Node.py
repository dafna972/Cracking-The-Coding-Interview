class Node:
    def __init__(self, data = None, left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):   
        if self.left_child == None:
            return str(self.data)  
        elif self.right_child == None:
            return str(self.left_child) + str(self.data)
        else:
            return str(self.left_child) + str(self.data) + str(self.right_child)

    