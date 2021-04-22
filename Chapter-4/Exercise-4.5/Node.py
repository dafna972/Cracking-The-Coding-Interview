class Node:
    def __init__(self, value = None, left_child = None, right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
    
    def max(self):
        if self.right_child == None:
            return self.value
        else:
            return self.right_child.max()
    
    def min(self):
        if self.left_child == None:
            return self.value
        else:
            return self.left_child.min()

    def __str__(self):   
        if self.left_child == None:
            return str(self.value)  
        elif self.right_child == None:
            return str(self.left_child) + str(self.value)
        else:
            return str(self.left_child) + str(self.value) + str(self.right_child)

    